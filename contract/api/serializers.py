from rest_framework import serializers
from contract.models import Contract, Customer, Installment
from contract.api.selectors import customer_list, contract_list
from account.api.selectors import user_list
from account.api.serializers import UserReadSerializer
from product.api.selectors import product_list
from product.api.serializers import ProductSerializer
from company.api.serializers import OfficeSerializer
from company.api.selectors import office_list

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'type', 'email', 'phone_number_1', 'phone_number_2', 'address']

class ContractSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)
    office_id = serializers.PrimaryKeyRelatedField(
        queryset = office_list(), source="office", write_only=True
    )

    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = customer_list(), source="customer", write_only=True
    )

    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = product_list(), source="product", write_only=True
    )

    responsible_employee = UserReadSerializer(read_only=True)
    responsible_employee_id = serializers.PrimaryKeyRelatedField(
        queryset = user_list(), source="responsible_employee", write_only=True
    )

    class Meta:
        model = Contract
        fields = ['id', 'office', 'office_id', 'customer', 'customer_id', 'product', 'product_id', 'product_quantity', 'total_amount', 'remaining_payment', 'loan_term', 'initial_payment', 'contract_start_date', 'responsible_employee', 'responsible_employee_id', 'contract_type']

class InstallmentSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only=True)
    contract_id = serializers.PrimaryKeyRelatedField(
        queryset = contract_list(), source="contract", write_only=True
    )

    class Meta:
        model = Installment
        fields = ['id', 'contract', 'contract_id', 'amount', 'payment_date', 'paid_date', 'type']
