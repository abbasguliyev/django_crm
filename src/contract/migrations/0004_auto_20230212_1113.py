# Generated by Django 3.2.16 on 2023-02-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contract_contract_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phonde_number_1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phonde_number_2',
        ),
        migrations.RemoveField(
            model_name='installment',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number_1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='phone number'),
        ),
    ]