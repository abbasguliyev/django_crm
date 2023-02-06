from rest_framework import serializers
from warehouse.models import Warehouse, Stock
from warehouse.api.selectors import warehouse_list
from product.api.serializers import ProductSerializer
from product.api.selectors import product_list

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address']

class StockSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)
    warehouse_id = serializers.PrimaryKeyRelatedField(
        queryset = warehouse_list(), source = "warehouse", write_only=True
    )

    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = product_list(), source = "product", write_only=True
    )

    class Meta:
        model = Stock
        fields = ['id', 'warehouse', 'warehouse_id', 'product', 'product_id', 'quantity']
