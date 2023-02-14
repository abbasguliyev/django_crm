from django.contrib import admin
from contract.models import Customer, Contract, Installment
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "email", "phone_number_1", "phone_number_2", "address")
    list_display_links  = ("id", "name")
    
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "product", "total_amount", 'discount', "remaining_payment", "loan_term", "initial_payment", "contract_start_date", "responsible_employee", "contract_type")
    list_display_links  = ("id",)
    
    
@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "amount", "payment_date", "paid_date", "type")
    list_display_links  = ("id",)
    list_filter = ('contract', 'type')
    