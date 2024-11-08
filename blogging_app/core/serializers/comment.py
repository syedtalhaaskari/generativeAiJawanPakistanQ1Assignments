from django.contrib.auth.models import User
from rest_framework import serializers

from core.models.comment import Comment
from core.models.post import Post
from user_auth.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }