from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models.comment import Comment
from core.serializers.comment import CommentSerializer

from core.permissions import CommentPermissions

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('post').select_related('user').all()
    serializer_class = CommentSerializer
    permission_classes = (CommentPermissions,)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()