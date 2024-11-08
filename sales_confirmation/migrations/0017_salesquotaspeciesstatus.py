# Generated by Django 4.2.9 on 2024-10-27 07:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0007_delete_salesquotaspeciesstatus'),
        ('sales_confirmation', '0016_alter_salesconfirmationproposal_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesQuotaSpeciesStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('provision_sales', 'Provision Sales'), ('confirmed', 'Confirmed'), ('declined', 'Declined'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_sales_area_status_set', to='bm_hunting_settings.huntingarea')),
                ('quota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_sales_quota_status_set', to='bm_hunting_settings.quota')),
                ('sales_proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_sales_inquiry_status_set', to='sales_confirmation.salesconfirmationproposal')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_sales_species_status_set', to='bm_hunting_settings.species')),
            ],
            options={
                'verbose_name_plural': 'Sales Quota Species Status',
                'db_table': 'sales_quota_species_status',
            },
        ),
    ]
