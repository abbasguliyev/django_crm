import pandas as pd
from django.utils import timezone
from contract.models import Customer, Contract, Installment
from contract.api.selectors import customer_list, contract_list, installment_list
from warehouse.api.decorators import reduce_product_from_stock_decorator
from cashbox.api.decorators import contract_cashbox_decorator
from cashbox.api.selectors import cashbox_list
from cashbox.api.services import create_cashflow

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

@contract_cashbox_decorator
@reduce_product_from_stock_decorator
def create_contract(
    *, office, 
    customer, 
    product,
    product_quantity: int = 1,
    loan_term: int = 0,
    initial_payment: float = 0,
    contract_start_date: str = None,
    responsible_employee: str = None,
    contract_type: str,
    total_amount: float = 0,
    remaining_payment: float = 0,
    discount: float = 0
) -> Contract:
    total_amount = (product.price * product_quantity) - discount
    remaining_payment = total_amount - initial_payment

    obj = Contract.objects.create(
        office=office, customer=customer, loan_term=loan_term, initial_payment=initial_payment,
        contract_start_date=contract_start_date, responsible_employee=responsible_employee,
        contract_type=contract_type, product=product, total_amount=total_amount,
        remaining_payment=remaining_payment, discount=discount
    )
    obj.full_clean()
    obj.save()
    return obj

def update_contract(instance, **data) -> Contract:
    obj = contract_list().filter(pk=instance.pk).update(**data)
    return obj


def create_installment_for_loan_term(
    *, loan_term, 
    inc_month, 
    payment_amount_for_last_month, 
    payment_amount_for_month,
    contract,
    now
):
    i = 1
    while i <= loan_term:
        if i == loan_term:
            if now.day < 29:
                Installment.objects.create(
                    contract=contract,
                    payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{now.day}",
                    amount=payment_amount_for_last_month
                ).save()
            elif now.day == 31 or now.day == 30 or now.day == 29:
                if inc_month[i].day <= now.day:
                    Installment.objects.create(
                        contract=contract,
                        payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                        amount=payment_amount_for_last_month
                    ).save()
                elif inc_month[i].day > now.day:
                    Installment.objects.create(
                        contract=contract,
                        payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{now.day}",
                        amount=payment_amount_for_last_month
                    ).save()
        else:
            if now.day < 29:
                Installment.objects.create(
                    contract=contract,
                    payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{now.day}",
                    amount=payment_amount_for_month
                ).save()
            elif now.day == 31 or now.day == 30 or now.day == 29:
                if inc_month[i].day <= now.day:
                    Installment.objects.create(
                        contract=contract,
                        payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{inc_month[i].day}",
                        amount=payment_amount_for_month
                    ).save()
                if inc_month[i].day > now.day:
                    Installment.objects.create(
                        contract=contract,
                        payment_date=f"{inc_month[i].year}-{inc_month[i].month}-{now.day}",
                        amount=payment_amount_for_month
                    ).save()
        i += 1

def create_installment(contract):
    loan_term = contract.loan_term

    if contract.contract_type == "Installment":
        now = contract.contract_start_date
        inc_month = pd.date_range(now, periods=loan_term+1, freq='M')
        initial_payment = contract.initial_payment

        if initial_payment is None:
            initial_payment = 0

        total_amount = contract.total_amount

        total_payment_amount_for_month = total_amount - initial_payment

        payment_amount_for_month = total_payment_amount_for_month // loan_term

        debt = payment_amount_for_month * (loan_term - 1)
        payment_amount_for_last_month = total_payment_amount_for_month - debt

        if loan_term > 0:    
            create_installment_for_loan_term(
                loan_term=loan_term,
                inc_month=inc_month,
                payment_amount_for_last_month=payment_amount_for_last_month,
                payment_amount_for_month=payment_amount_for_month,
                contract=contract,
                now=now
            )

def update_installment(instance, **data) -> Installment:
    type = data.get('type')
    if type is not None:
        pay_installment(instance=instance)

    obj = installment_list().filter(pk=instance.pk).update(**data)
    return obj

def pay_installment(instance):
    instance.paid_date = timezone.now
    instance.type = "Finished"
    instance.save()
    instance.contract.remaining_payment = instance.contract.remaining_payment - instance.amount
    instance.contract.save()

    cashbox = cashbox_list().filter(office=instance.contract.office).last()
    cashbox.balance = cashbox.balance + instance.amount
    cashbox.save()

    create_cashflow(
        office=instance.contract.office, 
        customer=instance.contract.customer, 
        personal=instance.contract.responsible_employee, 
        description="Pay Installment",
        balance=cashbox.balance,
        operation_style="INCOME",
        quantity=instance.amount
    )