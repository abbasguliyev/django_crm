from django.db.models.query import QuerySet
from cashbox.models import Cashbox, CashFlow

def cashbox_list() -> QuerySet[Cashbox]:
    qs = Cashbox.objects.select_related('office').all()
    return qs

def cashflow_list() -> QuerySet[CashFlow]:
    qs = CashFlow.objects.select_related('office', 'customer', 'personal', 'executor').all()
    return qs