from rest_framework import serializers
from company.models import Company, Office
from company.api.selectors import company_list

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only = True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset = company_list(), source="company", write_only=True
    )
    class Meta:
        model = Office
        fields = ['id', 'name', 'company', 'company_id', 'is_main', 'address']
