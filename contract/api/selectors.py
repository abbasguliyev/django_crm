from django.db.models.query import QuerySet
from contract.models import Contract, Customer, Installment

def customer_list() -> QuerySet[Customer]:
    qs = Customer.objects.all()
    return qs

def contract_list() -> QuerySet[Contract]:
    qs = Contract.objects.select_related('customer', 'responsible_employee').all()
    return qs

def installment_list() -> QuerySet[Installment]:
    qs = Installment.objects.select_related('contract').all()
    return qs