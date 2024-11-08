from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from core.models.category import Category
from core.serializers.category import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method != 'GET':
            return (IsAdminUser(),)
        return super().get_permissions()