from django.db.models.query import QuerySet
from company.models import Company, Office

def company_list() -> QuerySet[Company]:
    qs = Company.objects.all()
    return qs

def office_list() -> QuerySet[Office]:
    qs = Office.objects.select_related('company').all()
    return qs