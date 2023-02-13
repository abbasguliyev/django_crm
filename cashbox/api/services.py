from cashbox.models import Cashbox, CashFlow
from cashbox.api.selectors import cashbox_list, cashflow_list

def create_cashbox(
    *, office,
    name: str,
    balance: float = 0
) -> Cashbox:
    obj = Cashbox.objects.create(office=office, name=name, balance=balance)
    obj.full_clean()
    return obj

def update_cashbox(instance, **data) -> Cashbox:
    obj = cashbox_list().filter(pk=instance.pk).update(**data)
    return obj

def create_cashflow(
    *, office,
    customer,
    personal,
    description: str = None,
    balance: float = 0,
    executor,
    operation_style: str = None,
    quantity: float = 0
) -> CashFlow:
    obj = CashFlow.objects.create(
        office=office,
        customer=customer,
        personal=personal,
        description=description,
        balance=balance,
        executor=executor,
        operation_style=operation_style,
        quantity=quantity
    )
    obj.full_clean()
    return obj

def update_cashflow(instance, **data) -> CashFlow:
    obj = cashflow_list().filter(pk=instance.pk).update(**data)
    return obj