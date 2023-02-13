from django.db.models.signals import post_save
from django.dispatch import receiver
from company.models import Office
from cashbox.api.services import create_cashbox
from cashbox.api.selectors import cashbox_list

@receiver(post_save, sender=Office)
def create_cashbox_signal(sender, instance, created, **kwargs):
    if created:
        cashbox_count = cashbox_list().filter(office=instance).count()
        if cashbox_count == 0:
            create_cashbox(office=instance, name=f"Cashbox of {instance.name} office", balance=0)
