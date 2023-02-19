import django_filters
from cashbox.models import Cashbox, CashFlow

class CashboxFilter(django_filters.FilterSet):
    class Meta:
        model = Cashbox
        fields = {
            'office': ['exact'],
            'name': ['exact'],
            'balance': ['exact'],
        }

class CashFlowFilter(django_filters.FilterSet):
    class Meta:
        model = CashFlow
        fields = {
            'office': ['exact'],
            'customer': ['exact'],
            'personal': ['exact'],
            'description': ['exact', 'icontains'],
            'balance': ['exact'],
            'executor': ['exact'],
            'operation_style': ['exact'],
            'quantity': ['exact']
        }
        