import django_filters
from warehouse.models import Warehouse, Stock

class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ['name', 'address']

class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = ['warehouse', 'product', 'quantity']