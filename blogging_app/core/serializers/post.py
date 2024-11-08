from django.contrib.auth.models import User
from rest_framework import serializers

from user_auth.serializers import UserSerializer
from core.serializers.category import CategorySerializer
from core.serializers.comment import CommentSerializer
from core.serializers.like import LikeSerializer
from ..models.post import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True},
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['owner'] = UserSerializer(instance.owner).data
        rep['authors'] = UserSerializer(instance.authors.all(), many=True).data
        rep['category'] = CategorySerializer(instance.category.all(), many=True).data
        rep['comment'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['like'] = LikeSerializer(instance.likes.all(), many=True).data
        return rep