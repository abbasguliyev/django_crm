from django.db.models.signals import post_save
from django.dispatch import receiver
from company.models import Office
from warehouse.api.services import create_warehouse
from warehouse.api.selectors import warehouse_list

@receiver(post_save, sender=Office)
def create_warehouse_signal(sender, instance, created, **kwargs):
    if created:
        warehouse_count = warehouse_list().filter(office=instance).count()
        if warehouse_count == 0:
            create_warehouse(office=instance, name=f"Warehouse of {instance.name} office", address=instance.address)
