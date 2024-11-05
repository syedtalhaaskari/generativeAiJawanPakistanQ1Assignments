from rest_framework import serializers

class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    contact = serializers.CharField(required=False)