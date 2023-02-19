from rest_framework.exceptions import ValidationError
from warehouse.models import Warehouse, Stock
from warehouse.api.selectors import warehouse_list, stock_list

def create_warehouse(*, office, name: str, address: str) -> Warehouse:
    obj = Warehouse.objects.create(office=office, name=name, address=address)
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

def reduce_product_from_stock(stock: Stock, product_quantity: int) -> int:
    stock.quantity = stock.quantity - product_quantity
    if stock.quantity < product_quantity:
        raise ValidationError(detail="There are not enough products in stock")
    stock.quantity = stock.quantity - product_quantity
    stock.save()
    if stock.quantity == 0:
        stock.delete()
    return stock.quantity

def add_product_to_stock(stock: Stock, product_quantity: int) -> int:
    stock.quantity = stock.quantity + product_quantity
    stock.save()
    return stock.quantity