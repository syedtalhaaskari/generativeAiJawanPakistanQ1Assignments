from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.models.category import Category
from core.serializers.category import CategorySerializer as CS

@api_view(['GET', 'POST'])
def get_or_create_category(request: Request):
    if request.method == 'GET':
        category_obj = Category.objects.all()

        category_serializer = CS(category_obj, many=True)

        return Response(data=category_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        category_serializer = CS(data=request.data)

        if category_serializer.is_valid():
            Category.objects.create(**category_serializer.validated_data)
            return Response(data=category_serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_category(request: Request, id):
    try:
        category = Category.objects.get(pk=id)

        if request.method == 'GET':
            category_serializer = CS(category)

            return Response(data=category_serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            category_serializer = CS(category, data=request.data)

            if category_serializer.is_valid():
                for key, value in category_serializer.validated_data.items():
                    setattr(category, key, value)
                category.save()
                return Response(data=category_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            category.delete()
            return Response('Category Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response(data={"error": 'Invalid Category'}, status=status.HTTP_400_BAD_REQUEST)