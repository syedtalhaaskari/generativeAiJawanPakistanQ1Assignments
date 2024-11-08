from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count, Sum, Avg, F, Q

from core.models.post import Post
from core.models.comment import Comment
from core.models.like import Like
from core.serializers.post import PostSerializer
from core.permissions import PostPermissions

class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('owner').prefetch_related('authors').prefetch_related('category').all()
    serializer_class = PostSerializer
    permission_classes = (PostPermissions,)

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    @action(detail=False, methods=['GET'])
    def summary(self, request: Request):
        response_obj = {
            "total_posts": 0,
            "total_comments": 0,
            "total_likes": 0,
        }
        if request.user.groups.filter(name='SuperUser').exists() or request.user.is_superuser:
            response_obj["total_posts"] = Post.objects.all().__len__()
            response_obj["total_comments"] = Comment.objects.all().__len__()
            response_obj["total_likes"] = Like.objects.all().__len__()
        else:
            response_obj["total_posts"] = Post.objects.filter(owner=request.user).all().__len__()
            response_obj["total_comments"] = Comment.objects.filter(user=request.user).all().__len__()
            response_obj["total_likes"] = Like.objects.filter(user=request.user).all().__len__()
        return Response(data=response_obj, status=status.HTTP_200_OK)