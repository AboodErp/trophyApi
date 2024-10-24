# Generated by Django 4.2.9 on 2024-10-23 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bm_hunting_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone'), ('address', 'Address')], max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Types',
                'db_table': 'contact_types',
            },
        ),
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
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bm_hunting_settings.country')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bm_hunting_settings.nationalities')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Entities',
                'db_table': 'entities',
            },
        ),
        migrations.CreateModel(
            name='EntityCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Entity Categories',
                'db_table': 'entity_categories',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('bank_transfer', 'Bank Transfer'), ('credit_card', 'Credit Card'), ('cash', 'Cash')], default='bank_transfer', max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Payment Methods',
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='SalesInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_inquiry_entity_set', to='sales.entity')),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bm_hunting_settings.seasons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_inquiry_user_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sales Inquiries',
                'db_table': 'sales_inquiries',
            },
        ),
        migrations.CreateModel(
            name='SalesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_payment_currency_set', to='bm_hunting_settings.currency')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_payment_entity_set', to='sales.entity')),
                ('payment_method_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_payment_method_set', to='sales.paymentmethod')),
            ],
            options={
                'verbose_name_plural': 'Sales Payments',
                'db_table': 'sales_payments',
            },
        ),
        migrations.CreateModel(
            name='SalesIquiryPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_experience', models.TextField(blank=True, max_length=500, null=True)),
                ('preferred_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('no_of_hunters', models.IntegerField(default=1)),
                ('no_of_observers', models.IntegerField(default=0)),
                ('no_of_days', models.IntegerField(default=0)),
                ('no_of_companions', models.IntegerField(default=0)),
                ('special_requests', models.CharField(blank=True, max_length=100, null=True)),
                ('budget_estimation', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('accommodation_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bm_hunting_settings.accommodationtype')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_inquiry_payment_method_set', to='sales.paymentmethod')),
                ('sales_inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_inquiry_preference_set', to='sales.salesinquiry')),
            ],
            options={
                'verbose_name_plural': 'Sales Inquiry Preferences',
                'db_table': 'sales_inquiry_preferences',
            },
        ),
        migrations.CreateModel(
            name='SalesInquirySpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('sales_inquiry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_inquiry_species_set', to='sales.salesinquiry')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_sales_inquiry_set', to='bm_hunting_settings.species')),
            ],
            options={
                'verbose_name_plural': 'Sales Inquiry Species',
                'db_table': 'sales_inquiry_species',
            },
        ),
        migrations.CreateModel(
            name='SalesInquiryArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hunting_inquiry_area_set', to='bm_hunting_settings.huntingarea')),
                ('sales_inquiry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hunting_inquiry_area_set', to='sales.salesinquiry')),
            ],
            options={
                'verbose_name_plural': 'Hunting Inquiry Areas',
                'db_table': 'sales_inquiry_areas',
            },
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_number', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('entity_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='identity', to='sales.entity')),
                ('identity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identity_type', to='bm_hunting_settings.identitytype')),
            ],
            options={
                'verbose_name_plural': 'Identities',
                'db_table': 'identities',
            },
        ),
        migrations.CreateModel(
            name='EntityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_category', to='sales.entitycategories')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_category', to='sales.entity')),
            ],
            options={
                'verbose_name_plural': 'Entity Categories',
                'db_table': 'entity_category',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('contactable', models.BooleanField(default=True)),
                ('contact_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_type_set', to='sales.contacttype')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_contacts_set', to='sales.entity')),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'db_table': 'contacts',
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
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forWho', models.CharField(max_length=100, null=True)),
                ('document_type', models.CharField(choices=[('Passport_Copy', 'Travel Packet(Passport Copy)'), ('Passport_Photo', 'Travel Packet(Passport  Photo'), ('Visa', 'Visa'), ('Gun Permits', 'Gun Permits'), ('CITES Documentation', 'CITES Documentation')], max_length=100)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_document_set', to='sales.entity')),
            ],
            options={
                'verbose_name_plural': 'Client Documents',
                'db_table': 'documents',
                'unique_together': {('forWho', 'document_type')},
            },
        ),
    ]
