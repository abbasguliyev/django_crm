from rest_framework import serializers
from cashbox.models import CashFlow, Cashbox
from company.api.serializers import OfficeSerializer
from company.api.selectors import office_list
from contract.api.serializers import CustomerSerializer
from contract.api.selectors import customer_list
from account.api.serializers import UserReadSerializer
from account.api.selectors import user_list

class CashboxSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only = True)
    office_id = serializers.PrimaryKeyRelatedField(
        queryset = office_list(), source="office", write_only=True
    )

    class Meta:
        model = Cashbox
        fields = ['id', 'name', 'office', 'office_id', 'balance', 'created_at']

class CashFlowSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only = True)
    office_id = serializers.PrimaryKeyRelatedField(
        queryset = office_list(), source="office", write_only=True
    )

    customer = CustomerSerializer(read_only = True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = customer_list(), source="customer", write_only=True
    )

    personal = UserReadSerializer(read_only = True)
    personal_id = serializers.PrimaryKeyRelatedField(
        queryset = user_list(), source="personal", write_only=True
    )

    executor = UserReadSerializer(read_only = True)
    executor_id = serializers.PrimaryKeyRelatedField(
        queryset = user_list(), source="executor", write_only=True
    )

    class Meta:
        model = CashFlow
        fields = [
            'id', 'office', 'office_id', 'customer', 
            'customer_id', 'personal', 'personal_id',
            'executor', 'executor_id', 'description', 
            'balance', 'operation_style', 'quantity',
            'created_at'
        ]
