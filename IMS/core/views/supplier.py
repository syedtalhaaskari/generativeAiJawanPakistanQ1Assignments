from django.db.models import Count, Q, F

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from core.models.supplier import Supplier
from core.models.product import Product
from core.serializers.supplier import SupplierSerializer as SS

@api_view(['GET', 'POST'])
def get_or_create_supplier(request: Request):
    if request.method == 'GET':
        supplier_obj = Supplier.objects.all()

        serializer = SS(supplier_obj, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SS(data=request.data)

        if serializer.is_valid():
            Supplier.objects.create(**serializer.validated_data)

            return Response('Success', status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_supplier(request: Request, id):
    try:
        supplier = Supplier.objects.get(pk=id)

        if request.method == 'GET':
            serializer = SS(supplier)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            data = request.data
            serializer = SS(supplier, data=data)

            if serializer.is_valid():
                product_ids = data.get('product_ids')
                if product_ids is not None:
                    product_obj = Product.objects.filter(id__in=product_ids).all()
                    if len(product_obj) != len(product_ids):
                        return Response(data="One or more of product id(s) are invalid", status=status.HTTP_400_BAD_REQUEST)
                    supplier.product_supplier.set(product_ids)
                for key, value in serializer.validated_data.items():
                    setattr(supplier, key, value)
                supplier.save()
                return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            supplier.delete()
            return Response('Supplier deleted successfully', status=status.HTTP_204_NO_CONTENT)
    except Supplier.DoesNotExist:
        return Response(data={"error": 'Invalid Supplier'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(http_method_names=["GET"])
def show_supplier_metrics(request: Request):
    try:
        response_obj = {
            "highest_products_suppliers": [],
	        "lowest_products_suppliers": [],
            "suppliers": [],
        }

        products_per_supplier = Supplier.objects.prefetch_related('product_supplier').prefetch_related('product_supplier__category').annotate(total_products=Count("product_supplier__supplier", filter=Q(product_supplier__supplier=F('id')))).order_by('-total_products').all()
        highest = products_per_supplier[0].total_products
        lowest = products_per_supplier[len(products_per_supplier) - 1].total_products

        for item in products_per_supplier:
            if highest == item.total_products:
                response_obj["highest_products_suppliers"].append(item.id)
            elif lowest == item.total_products:
                response_obj["lowest_products_suppliers"].append(item.id)

            supplier_obj = {
                "id": item.id,
                "name": item.name,
                "total_products": item.total_products,
                "supplied_products_by_categories": {}
            }

            products_list = item.product_supplier.select_related('category').all()
            for product_item in products_list:
                if (supplier_obj["supplied_products_by_categories"].get(product_item.category.name) is None):
                    supplier_obj["supplied_products_by_categories"][product_item.category.name] = []
                supplier_obj["supplied_products_by_categories"][product_item.category.name].append({
                    "id": product_item.id,
                    "name": product_item.name,
                    "price": product_item.price,
                    "quantity": product_item.quantity,
                    "category_id": product_item.category.id,
                })
            response_obj["suppliers"].append(supplier_obj)
        return Response(data=response_obj, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(data={"error": "Invalid Product"}, status=status.HTTP_400_BAD_REQUEST)