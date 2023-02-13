from django.db.models.signals import post_save
from django.dispatch import receiver
from company.models import Company
from company.api.services import create_office
from company.api.selectors import office_list

@receiver(post_save, sender=Company)
def create_main_office_signal(sender, instance, created, **kwargs):
    if created:
        office_count = office_list().filter(company=instance, is_main=True).count()
        if office_count == 0:
            create_office(company=instance, name=f"Main office of {instance.name} company", address=instance.address, is_main=True)
