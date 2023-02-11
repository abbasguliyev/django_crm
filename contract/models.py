from django.db import models
from django.utils.translation import gettext_lazy as _
from django_crm.utils.models import BaseModel
from django.utils import timezone
from django.contrib.auth import get_user_model

class Customer(BaseModel):
    PERSONAL = "Personal"
    COMPANY = "Company"

    TYPE_CHOICES = (
        (PERSONAL, "Personal"),
        (COMPANY, "Company")
    )

    name = models.CharField(_("name"), max_length=150)
    type = models.CharField(_("type"), max_length=100, choices=TYPE_CHOICES, default=PERSONAL)
    email = models.EmailField(_("email"), null=True, blank=True)
    phone_number_1 = models.CharField(_("phone number"), max_length=100, null=True, blank=True)
    phone_number_2 = models.CharField(_("phone number"), max_length=100, null=True, blank=True)
    address = models.TextField()

    class Meta:
        ordering = ('id',)

class Contract(BaseModel):
    CASH = "Cash"
    INSTALLMENT = "Installment"

    TYPE_CHOICES = (
        (CASH, "Cash"),
        (INSTALLMENT, "Installment")
    )

    customer = models.ForeignKey("contract.Customer", on_delete=models.CASCADE, related_name="contracts")
    loan_term = models.PositiveIntegerField(_("loan term"), default=0)
    initial_payment = models.DecimalField(_("initial payment"), max_digits=25, decimal_places=2, default=0)
    contract_start_date = models.DateField(_("contract starting date"), default=timezone.now)
    responsible_employee = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name="contracts", null=True, blank=True)
    contract_type = models.CharField(_("contract type"), max_length=100, choices=TYPE_CHOICES, default=CASH)

    class Meta:
        ordering = ('id',)

class Installment(BaseModel):
    CONTINUING = "Continuing"
    FINISHED = "Finished"

    TYPE_CHOICES = (
        (CONTINUING, "Continuing"),
        (FINISHED, "Finished")
    )

    contract = models.ForeignKey("contract.Contract", on_delete=models.CASCADE, related_name="installments")
    amount = models.DecimalField(_("amount to pay"), max_digits=25, decimal_places=2, default=0)
    paid_amount = models.DecimalField(_("paid amount"), max_digits=25, decimal_places=2, default=0)
    payment_date = models.DateField(_("payment date"), null=True, blank=True)
    paid_date = models.DateField(_("paid date"), null=True, blank=True)
    type = models.CharField(_("contract type"), max_length=100, choices=TYPE_CHOICES, default=CONTINUING)

    class Meta:
        ordering = ('id',)