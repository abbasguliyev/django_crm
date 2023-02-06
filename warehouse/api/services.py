from warehouse.models import Warehouse, Stock
from warehouse.api.selectors import warehouse_list, stock_list

def create_warehouse(*, name: str, address: str) -> Warehouse:
    obj = Warehouse.objects.create(name=name, address=address)
    obj.full_clean()
    return obj

def update_warehouse(instance, **data) -> Warehouse:
    obj = warehouse_list().filter(pk=instance.pk).update(**data)
    return obj

def create_stock(
    *, warehouse,
    product,
    quantity: int = 0
) -> Stock:
    obj = Stock.objects.create(warehouse=warehouse, product=product, quantity=quantity)
    obj.full_clean()
    return obj

def update_stock(instance, **data) -> Stock:
    obj = stock_list().filter(pk=instance.pk).update(**data)
    return obj
