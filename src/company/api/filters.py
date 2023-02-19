import django_filters
from company.models import Company, Office

class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'name': ['exact'],
            'address': ['exact'],
            'created_at': ['exact'],
        }

class OfficeFilter(django_filters.FilterSet):
    class Meta:
        model = Office
        fields = {
            'company': ['exact'],
            'name': ['exact'],
            'address': ['exact'],
            'is_main': ['exact'],
            'created_at': ['exact'],
        }
        