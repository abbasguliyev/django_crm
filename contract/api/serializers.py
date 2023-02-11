from rest_framework import serializers
from contract.models import Contract, Customer, Installment
from contract.api.selectors import customer_list, contract_list
from account.api.selectors import user_list

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'type', 'email', 'phone_number_1', 'phone_number_2', 'address']

class ContractSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = customer_list(), source="customer", write_only=True
    )

    responsible_employee = CustomerSerializer(read_only=True)
    responsible_employee_id = serializers.PrimaryKeyRelatedField(
        queryset = user_list(), source="responsible_employee", write_only=True
    )

    class Meta:
        model = Contract
        fields = ['id', 'customer', 'customer_id', 'loan_term', 'initial_payment', 'contract_start_date', 'responsible_employee', 'responsible_employee_id', 'contract_type']

class InstallmentSerializer(serializers.ModelSerializer):
    contract = CustomerSerializer(read_only=True)
    contract_id = serializers.PrimaryKeyRelatedField(
        queryset = contract_list(), source="contract", write_only=True
    )

    class Meta:
        model = Installment
        fields = ['id', 'contract', 'contract_id', 'amount', 'paid_amount', 'payment_date', 'paid_date', 'type']
