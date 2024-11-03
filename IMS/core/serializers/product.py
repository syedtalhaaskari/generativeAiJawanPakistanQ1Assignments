from rest_framework import serializers

from .category import CategorySerializer, CategoryMetricsSerializer
from .supplier import SupplierSerializer

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=9, decimal_places=4)
    quantity = serializers.IntegerField(min_value=0)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    supplier = SupplierSerializer(read_only=True, many=True)
    supplier_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

class ProductSupplierSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    supplier_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

class ProductMetricsSerializer(serializers.Serializer):
    total_products = serializers.IntegerField()
    category = serializers.DictField(child=CategoryMetricsSerializer())