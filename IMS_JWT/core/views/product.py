from datetime import datetime

from django.db.models import Count, Sum, Avg, F, Q

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from core.models.product import Product, Category, Supplier, ProductSupplier
from core.models.product_audit import ProductAudit
from core.serializers.product import ProductSerializer as PS
from core.serializers.product_audit import ProductAuditSerializer

@api_view(['GET', 'POST'])
def get_or_create_product(request: Request):
    if request.method == 'GET':
        params = request.query_params
        product_obj = Product.objects.select_related('category').prefetch_related('supplier')

        name = params.get('name')
        category_id = params.get('category_id')
        supplier_id = params.get('supplier_id')

        if name is not None:
            product_obj = product_obj.filter(name=name)
        if category_id is not None:
            product_obj = product_obj.filter(category_id=category_id)
        if supplier_id is not None:
            product_obj = product_obj.filter(supplier__id=supplier_id)
        
        products = product_obj.all()
        serializer = PS(products, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PS(data=request.data)

        if serializer.is_valid():
            supplier_ids = serializer.validated_data.pop('supplier_ids')

            suppliers_list = Supplier.objects.filter(id__in=supplier_ids).all()
            if len(suppliers_list) != len(supplier_ids):
                return Response(data="One or Supplier IDs are invalid", status=status.HTTP_400_BAD_REQUEST)

            category_obj = Category.objects.filter(id=serializer.validated_data.get('category_id')).first()
            if category_obj is None:
                return Response(data="Invalid Category ID", status=status.HTTP_400_BAD_REQUEST)

            product_obj = Product.objects.create(**serializer.validated_data)
            for supplier in suppliers_list:
                ProductSupplier.objects.create(
                    product=product_obj, 
                    supplier=supplier, 
                    quantity=serializer.validated_data['quantity']//len(suppliers_list)
                )
            audit_obj = request.data
            audit_obj['product_id'] = product_obj.id
            audit_obj['created_at'] = product_obj.created_at
            audit_obj['created_by'] = request.user
            audit_obj['supplier_ids'] = supplier_ids

            ProductAudit.objects.create(**audit_obj)

            return Response(data="Success", status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_product(request: Request, id):
    try:
        product = Product.objects.select_related('category').prefetch_related('supplier').get(pk=id)
        
        if request.method == 'GET':
            serializer = PS(product)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            data = request.data

            serializer = PS(product, data=data)

            if serializer.is_valid():
                supplier_ids = serializer.validated_data.pop('supplier_ids')
                         
                suppliers_list = Supplier.objects.filter(id__in=supplier_ids)
                if len(suppliers_list) != len(supplier_ids):
                    return Response(data="One or more of supplier id(s) are invalid", status=status.HTTP_400_BAD_REQUEST)
                
                category_obj = Category.objects.filter(id=serializer.validated_data['category_id'])

                if category_obj is None:
                    return Response(data="Invalid Category ID", status=status.HTTP_400_BAD_REQUEST)

                for key, value in serializer.validated_data.items():
                    setattr(product, key, value)
                product.save()

                product_suppliers_list = ProductSupplier.objects.filter(product=product).all()
                product_suppliers_list.delete()
                for supplier in suppliers_list:
                    ProductSupplier.objects.create(
                        product=product, 
                        supplier=supplier, 
                        quantity=serializer.validated_data['quantity']//len(suppliers_list)
                    )

                audit_obj = request.data
                audit_obj['product_id'] = product.id
                audit_obj['updated_at'] = product.updated_at
                audit_obj['updated_by'] = request.user
                audit_obj['supplier_ids'] = supplier_ids

                ProductAudit.objects.create(**audit_obj)

                return Response(data="Product Updated Successfully", status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            product_suppliers_list = ProductSupplier.objects.filter(product=product).all()
            product_suppliers_list.delete()

            audit_obj = {}
            audit_obj['product_id'] = product.id
            audit_obj['deleted_at'] = datetime.now()
            audit_obj['deleted_by'] = request.user

            print(audit_obj)

            ProductAudit.objects.create(**audit_obj)

            product.delete()

            return Response('Supplier Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response(data={"error": 'Invalid Product'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
@api_view(http_method_names=["GET"])
def show_product_metrics(request: Request):
    try:
        response_obj = {
            "total_products": 0,
            "category": {},
            "suppliers": [],
        }
        product_obj = Product.objects
        total_products = product_obj.count()

        response_obj["total_products"] = total_products

        group_categories = Category.objects.prefetch_related('product_category').annotate(
            products_count=Count("product_category"), 
            total_stock_quantity=Sum('product_category__quantity'),
            average_price=Avg('product_category__price'),
        )

        products_per_supplier = Supplier.objects.prefetch_related('product_supplier').annotate(total_products=Count("product_supplier__supplier", filter=Q(product_supplier__supplier=F('id')))).order_by('-total_products').all()

        for category in group_categories:
            response_obj['category'][category.name] = {
                "id": category.id,
                "products_count": category.products_count or 0,
                "total_stock_quantity": category.total_stock_quantity or 0,
                "average_price": category.average_price or 0,
            }

        for item in products_per_supplier:
            supplier_obj = {
                "id": item.id,
                "name": item.name,
                "total_products": item.total_products
            }

            response_obj["suppliers"].append(supplier_obj)

        return Response(data=response_obj, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(data={"error": "Invalid Product"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def show_product_audit(request: Request):
    try:
        product_audit_obj = ProductAudit.objects.all().order_by('-id')

        serializer = ProductAuditSerializer(product_audit_obj, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except ProductAudit.DoesNotExist:
        return Response(data={"error": "Invalid Product Audit"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def show_product_audit_by_product_id(request: Request, id: int):
    try:
        product_audit_obj = ProductAudit.objects.filter(product_id=id).order_by('-id')

        serializer = ProductAuditSerializer(product_audit_obj, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except ProductAudit.DoesNotExist:
        return Response(data={"error": "Invalid Product Audit"}, status=status.HTTP_400_BAD_REQUEST)