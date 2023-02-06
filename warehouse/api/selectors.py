from django.db.models.query import QuerySet
from warehouse.models import Warehouse, Stock

def warehouse_list() -> QuerySet[Warehouse]:
    qs = Warehouse.objects.all()
    return qs

def stock_list() -> QuerySet[Stock]:
    qs = Stock.objects.select_related('warehouse', 'product').all()
    return qs