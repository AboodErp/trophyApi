# Generated by Django 4.2.9 on 2024-10-08 08:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0014_remove_package_trophy_fees_list'),
        ('sales', '0002_rename_category_name_entitycategories_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contract Types',
                'db_table': 'contract_types',
            },
        ),
        migrations.CreateModel(
            name='SalesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method_type', models.CharField(choices=[('bank_transfer', 'Bank Transfer'), ('credit_card', 'Credit Card'), ('cash', 'Cash')], default='bank_transfer', max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_payment_entity_set', to='sales.entity')),
            ],
            options={
                'verbose_name_plural': 'Sales Payments',
                'db_table': 'sales_payments',
            },
        ),
        migrations.CreateModel(
            name='SalesConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_confirmation_entity_set', to='sales.entity')),
                ('hunting_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_confirmation_hunting_info_set', to='sales.entityhuntinginfos')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_confirmation_payment_set', to='sales.salespayment')),
            ],
            options={
                'verbose_name_plural': 'Sales Confirmations',
                'db_table': 'sales_confirmations',
            },
        ),
        migrations.CreateModel(
            name='PackageUpgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_hunters', models.IntegerField(default=0)),
                ('number_of_days', models.IntegerField(default=0)),
                ('number_companions', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_upgrade_entity_set', to='sales.entity')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_upgrade_package_type_set', to='bm_hunting_settings.package')),
                ('species_to_hunt', models.ManyToManyField(to='bm_hunting_settings.species')),
            ],
            options={
                'verbose_name_plural': 'Package Upgrades',
                'db_table': 'package_upgrades',
            },
        ),
        migrations.CreateModel(
            name='PackageCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_hunters', models.IntegerField(default=0)),
                ('number_of_days', models.IntegerField(default=0)),
                ('number_companions', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_customization_entity_set', to='sales.entity')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_customization_package_type_set', to='bm_hunting_settings.package')),
                ('species_to_hunt', models.ManyToManyField(to='bm_hunting_settings.species')),
            ],
            options={
                'verbose_name_plural': 'Package Customizations',
                'db_table': 'package_customizations',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=100, unique=True)),
                ('signed', models.DateTimeField(default=django.utils.timezone.now)),
                ('signed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirmed_sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_confirmed_sale_set', to='sales.salesconfirmation')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_type_set', to='sales.contracttype')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_entity_set', to='sales.entity')),
                ('hunting_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_hunting_info_set', to='sales.entityhuntinginfos')),
            ],
            options={
                'verbose_name_plural': 'Contracts',
                'db_table': 'contracts',
            },
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('account_holder_name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_details_entity_set', to='sales.entity')),
            ],
            options={
                'verbose_name_plural': 'Bank Details',
                'db_table': 'bank_details',
            },
        ),
    ]