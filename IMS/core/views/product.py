from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from core.models.product import Product, Category, Supplier
from core.serializers.product import ProductSerializer as PS

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
            product_obj = product_obj.product_supplier.filter(id=supplier_id)

        serializer = PS(product_obj.all(), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = PS(data=request.data)

        if serializer.is_valid():
            supplier_ids = serializer.validated_data.pop('supplier_ids')

            supplier_obj = Supplier.objects.filter(id__in=supplier_ids).all()
            if len(supplier_obj) != len(supplier_ids):
                return Response(data="One or Supplier IDs are invalid", status=status.HTTP_400_BAD_REQUEST)
            category_obj = Category.objects.filter(id=serializer.validated_data.get('category_id')).first()
            if category_obj is None:
                return Response(data="Invalid Category ID", status=status.HTTP_400_BAD_REQUEST)

            product_obj = Product.objects.create(**serializer.validated_data)
            product_obj.supplier.set(supplier_ids)

            return Response(data="Success", status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_product(request: Request, id):
    pass