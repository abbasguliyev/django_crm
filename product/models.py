from django.db import models
from django.utils.translation import gettext_lazy as _
from django_crm.utils.models import BaseModel

class Category(BaseModel):
    name = models.CharField(_("category name"), max_length=150, unique=True)

    class Meta:
        ordering = ('id',)

class Product(BaseModel):
    name = models.CharField(_("product name"), max_length=200)
    barcode = models.CharField(_("barcode"), max_length=200, unique=True)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=25, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    class Meta:
        ordering = ('id',)