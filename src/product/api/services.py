from product.models import Category, Product
from product.api.selectors import category_list, product_list

def create_category(*, name) -> Category:
    obj = Category.objects.create(name=name)
    obj.full_clean()
    return obj

def update_category(instance, **data) -> Category:
    obj = category_list().filter(pk=instance.pk).update(**data)
    return obj

def create_product(
    *, name: str,
    barcode: str,
    description: str,
    price: float = 0,
    category,
    image = None
) -> Product:
    obj = Product.objects.create(
        name=name, barcode=barcode, description=description, price=price, category=category, image=image
    )
    obj.full_clean()
    return obj

def update_product(instance, **data) -> Product:
    obj = product_list().filter(pk=instance.pk).update(**data)
    return obj
