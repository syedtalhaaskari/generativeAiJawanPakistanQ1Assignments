from rest_framework import serializers

from ..models.like import Like

class LikeSerializer(serializers.ModelSerializer):
    http_method_names = ['GET', 'DELETE']

    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
        }