from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django_crm.utils.models import BaseModel

class Cashbox(BaseModel):
    office = models.OneToOneField("company.Office", on_delete=models.CASCADE, related_name="cashbox")
    name = models.CharField(_("company name"), max_length=200)
    balance = models.DecimalField(_("balance"), max_digits=20, decimal_places=2)

    class Meta:
        ordering = ("id",)

class CashFlow(BaseModel):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

    OPERATION_STYLE_CHOICE = [
        (INCOME, "INCOME"),
        (EXPENSE, "EXPENSE"),
    ]
    office = models.ForeignKey('company.Office', on_delete=models.CASCADE, null=True, blank=True, related_name="cash_flows")
    customer = models.ForeignKey('contract.Customer', on_delete=models.CASCADE, null=True, blank=True, related_name="cash_flows")
    personal = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name="cash_flow_personals")
    description = models.TextField(_("description"), null=True, blank=True)
    balance = models.DecimalField(_("balance"), default=0, max_digits=20, decimal_places=0)
    executor = models.ForeignKey(get_user_model(), related_name="cash_flows", on_delete=models.CASCADE, null=True, blank=True)
    operation_style = models.CharField(_("operation_style"), max_length=100, choices=OPERATION_STYLE_CHOICE, default=None, null=True, blank=True)
    quantity = models.DecimalField(_("quantity"), default=0, max_digits=20, decimal_places=0)

    class Meta:
        ordering = ("-pk",)
