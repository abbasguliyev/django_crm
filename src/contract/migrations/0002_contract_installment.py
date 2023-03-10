# Generated by Django 3.2.16 on 2023-02-04 17:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('loan_term', models.PositiveIntegerField(default=0, verbose_name='loan term')),
                ('initial_payment', models.DecimalField(decimal_places=2, default=0, max_digits=25, verbose_name='initial payment')),
                ('contract_start_date', models.DateField(default=datetime.datetime(2023, 2, 4, 17, 4, 25, 609588, tzinfo=utc), verbose_name='contract starting date')),
                ('contract_type', models.CharField(choices=[('Cash', 'Cash'), ('Installment', 'Installment')], default='Cash', max_length=100, verbose_name='contract type')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='contract.customer')),
                ('responsible_employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=25, verbose_name='amount to pay')),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=25, verbose_name='paid amount')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='payment date')),
                ('paid_date', models.DateField(blank=True, null=True, verbose_name='paid date')),
                ('type', models.CharField(choices=[('Continuing', 'Continuing'), ('Finished', 'Finished')], default='Continuing', max_length=100, verbose_name='contract type')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='installments', to='contract.contract')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
