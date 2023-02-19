from cashbox.api.selectors import cashbox_list
from cashbox.api.services import create_cashflow

def contract_cashbox_decorator(func):
    def wrapper(*args, **kwargs):
        initial_payment = kwargs.get("initial_payment")
        contract_type = kwargs.get("contract_type")
        office = kwargs.get("office")
        customer = kwargs.get("customer")
        personal = kwargs.get("responsible_employee")
        discount = kwargs.get("discount")
        product = kwargs.get("product")
        product_quantity = kwargs.get("product_quantity")
        total = 0
        
        cashbox = cashbox_list().filter(office=office).last()
        
        if contract_type == "Cash":
            total = (product.price * product_quantity) - discount
            cashbox.balance = cashbox.balance + total
            cashbox.save()
        if contract_type == "Installment":
            total = initial_payment
            cashbox.balance = cashbox.balance + total
            cashbox.save()

        func(*args, **kwargs)

        create_cashflow(
            office=office, 
            customer=customer, 
            personal=personal, 
            description="Contract signature",
            balance=cashbox.balance,
            operation_style="INCOME",
            quantity=total
        )
    
    return wrapper
