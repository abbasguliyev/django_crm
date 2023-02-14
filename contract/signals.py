from django.db.models.signals import post_save
from django.dispatch import receiver
from contract.models import Contract
from contract.api.services import create_installment
from contract.api.selectors import installment_list

@receiver(post_save, sender=Contract)
def create_installment_signal(sender, instance, created, **kwargs):
    if created:
        create_installment(contract=instance)