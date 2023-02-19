from rest_framework.exceptions import ValidationError
from warehouse.api.selectors import warehouse_list, stock_list
from warehouse.api.services import reduce_product_from_stock

def reduce_product_from_stock_decorator(func):
    def wrapper(*args, **kwargs):
        quantity = kwargs.get('product_quantity')
        office = kwargs.get('office')
        product = kwargs.get('product')
        
        if quantity is not None:
            warehouse = warehouse_list().filter(office=office).last()
            stock = stock_list().filter(warehouse=warehouse, product=product).last()
            if stock is None:
                raise ValidationError(detail="There are not enough products in stock")
            reduce_product_from_stock(stock=stock, product_quantity=quantity)

        func(*args, **kwargs)
    return wrapper