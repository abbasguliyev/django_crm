import django_filters
from company.models import Company

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = ['name']