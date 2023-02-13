from django.db.models.signals import post_save
from django.dispatch import receiver
from contract.models import Contract
from contract.api.services import create_installment
from contract.api.selectors import installment_list

@receiver(post_save, sender=Contract)
def create_installment(sender, instance, created, **kwargs):
    if created:
        loan_term = instance.loan_term
        