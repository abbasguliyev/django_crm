from django.db.models.query import QuerySet
from company.models import Company

def company_list() -> QuerySet[Company]:
    qs = Company.objects.all()
    return qs