from rest_framework import serializers
from warehouse.models import Warehouse, Stock
from warehouse.api.selectors import warehouse_list, stock_list
from product.api.serializers import ProductSerializer
from product.api.selectors import product_list
from company.api.serializers import OfficeSerializer
from company.api.selectors import office_list

class WarehouseSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)
    office_id = serializers.PrimaryKeyRelatedField(
        queryset = office_list(), source = "office", write_only=True
    )

    class Meta:
        model = Warehouse
        fields = ['id', 'name', 'address', 'office', 'office_id']

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

class ChangeQuantityStockSerializer(serializers.Serializer):
    stock_id = serializers.PrimaryKeyRelatedField(
        queryset = stock_list()
    )
    quantity = serializers.IntegerField()