from company.models import Company
from company.api.selectors import company_list

def create_company(*, name, logo) -> Company:
    obj = Company.objects.create(name=name, logo=logo)
    obj.full_clean()
    return obj

def update_company(instance, **data) -> Company:
    obj = company_list().filter(pk=instance.pk).update(**data)
    return obj