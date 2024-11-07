from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            # "id",
            # "posts",
            # "comments",
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            # "user_permissions",
        ]
        extra_kwargs = {
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
        }

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
        }