from django.db import models
from django.utils.translation import gettext_lazy as _
from django_crm.utils.models import BaseModel

class Company(BaseModel):
    name = models.CharField(_("company name"), max_length=200)
    logo = models.ImageField(upload_to="company/logo/", null=True, blank=True)
    address = models.TextField()

class Office(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="offices")
    name = models.CharField(_("company name"), max_length=200)
    is_main = models.BooleanField(default=False) 
    address = models.TextField()

    class Meta:
        ordering = ("id",)
