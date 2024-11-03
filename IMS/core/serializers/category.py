from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

class CategoryMetricsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    products_count = serializers.IntegerField()
    total_stock_quantity = serializers.IntegerField()
    average_price = serializers.DecimalField(max_digits=9, decimal_places=4)