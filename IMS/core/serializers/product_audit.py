from rest_framework import serializers

class ProductAuditSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=4, required=False)
    quantity = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(required=False)
    supplier_ids = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    created_by = serializers.CharField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    updated_by = serializers.CharField(required=False)
    deleted_at = serializers.DateTimeField(required=False)
    deleted_by = serializers.CharField(required=False)