# Generated by Django 4.2.9 on 2024-10-26 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_confirmation', '0013_alter_salesconfirmationproposalstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesconfirmationproposalstatus',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('provision_sales', 'Provision Sales'), ('confirmed', 'Confirmed'), ('declined', 'Declined'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=255, null=True, validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
    ]
