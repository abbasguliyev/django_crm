from django.db.models.query import QuerySet
from product.models import Product, Category

def category_list() -> QuerySet[Category]:
    qs = Category.objects.all()
    return qs

def product_list() -> QuerySet[Product]:
    qs = Product.objects.select_related('category').all()
    return qs