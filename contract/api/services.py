from contract.models import Customer, Contract, Installment
from contract.api.selectors import customer_list, contract_list, installment_list

def create_customer(
    *, name: str, 
    type: str,
    email: str = None,
    phone_number_1: str = None,
    phone_number_2: str = None,
    address: str
) -> Customer:
    obj = Customer.objects.create(
        name=name, type=type, email=email,
        phone_number_1=phone_number_1, phone_number_2=phone_number_2,
        address=address
    )
    obj.full_clean()
    return obj

def update_customer(instance, **data) -> Customer:
    obj = customer_list().filter(pk=instance.pk).update(**data)
    return obj

def create_contract(
    *, customer, 
    loan_term: int = 0,
    initial_payment: float = 0,
    contract_start_date: str = None,
    responsible_employee: str = None,
    contract_type: str
) -> Contract:
    obj = Contract.objects.create(
        customer=customer, loan_term=loan_term, initial_payment=initial_payment,
        contract_start_date=contract_start_date, responsible_employee=responsible_employee,
        contract_type=contract_type
    )
    obj.full_clean()
    return obj

def update_contract(instance, **data) -> Contract:
    obj = contract_list().filter(pk=instance.pk).update(**data)
    return obj


def create_installment(
    *, contract, 
    amount: int = 0,
    paid_amount: float = 0,
    payment_date: str = None,
    paid_date: str = None,
    type: str
) -> Installment:
    obj = Installment.objects.create(
        contract=contract, amount=amount, paid_amount=paid_amount,
        payment_date=payment_date, paid_date=paid_date,
        type=type
    )
    obj.full_clean()
    return obj

def update_installment(instance, **data) -> Installment:
    obj = installment_list().filter(pk=instance.pk).update(**data)
    return obj