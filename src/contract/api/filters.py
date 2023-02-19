import django_filters
from contract.models import Contract, Customer, Installment

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            "name": ['exact', 'icontains'],
            "type": ['exact', 'icontains'],
            "email": ['exact', 'icontains'],
            "phone_number_1": ['exact', 'icontains'],
            "phone_number_2": ['exact', 'icontains'],
            "address": ['exact', 'icontains'],
        }

class ContractFilter(django_filters.FilterSet):
    class Meta:
        model = Contract
        fields = {
            "office": ['exact'],
            "customer": ['exact'],
            "customer__name": ['exact', 'icontains'],
            "customer__email": ['exact', 'icontains'],
            "loan_term": ['exact'],
            "initial_payment": ['exact', 'gte', 'lte'],
            "contract_start_date": ['exact', 'gte', 'lte'],
            "responsible_employee": ['exact'],
            "contract_type": ['exact'],
            "product": ['exact'],
            "product_quantity": ['exact'],
            "total_amount": ['exact'],
            "remaining_payment": ['exact'],
            "discount": ['exact'],
        }

class InstallmentFilter(django_filters.FilterSet):
    class Meta:
        model = Installment
        fields = {
            "contract": ['exact'],
            "amount": ['exact'],
            "payment_date": ['exact', 'gte', 'lte'],
            "paid_date": ['exact', 'gte', 'lte'],
            "type": ['exact'],
        }
