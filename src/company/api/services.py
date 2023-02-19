from company.models import Company, Office
from company.api.selectors import company_list, office_list

def create_company(*, name, logo, address) -> Company:
    obj = Company.objects.create(name=name, logo=logo, address=address)
    obj.full_clean()
    return obj

def update_company(instance, **data) -> Company:
    obj = company_list().filter(pk=instance.pk).update(**data)
    return obj

def create_office(*, name, company, is_main: bool=False, address) -> Office:
    obj = Office.objects.create(name=name, company=company, is_main=is_main, address=address)
    obj.full_clean()
    return obj

def update_office(instance, **data) -> Office:
    obj = office_list().filter(pk=instance.pk).update(**data)
    return obj