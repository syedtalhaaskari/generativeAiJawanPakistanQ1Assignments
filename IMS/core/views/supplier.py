from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from core.models.supplier import Supplier
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
            serializer = SS(supplier, data=request.data)
            if serializer.is_valid():
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