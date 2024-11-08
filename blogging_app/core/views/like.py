from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models.like import Like
from core.serializers.like import LikeSerializer

from core.permissions import LikePermissions

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.select_related('post').select_related('user').all()
    serializer_class = LikeSerializer
    permission_classes = (LikePermissions,)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()