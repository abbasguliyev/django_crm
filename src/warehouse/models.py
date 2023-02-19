from django.db import models
from django.utils.translation import gettext_lazy as _
from django_crm.utils.models import BaseModel
from django.utils import timezone
from django.contrib.auth import get_user_model

class Warehouse(BaseModel):
    name = models.CharField(_("warehouse name"), max_length=200)
    office = models.ForeignKey("company.Office", on_delete=models.CASCADE, related_name="warehouses")
    address = models.TextField()

    class Meta:
        ordering = ('id',)

class Stock(BaseModel):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="stocks")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="stocks")
    quantity = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ('id',)