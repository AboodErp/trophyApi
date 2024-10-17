# Generated by Django 4.2.9 on 2024-10-16 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bm_hunting_settings', '0075_huntingpricelisttype'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='huntingpricelisttype',
            unique_together={('price_list', 'huting_type')},
        ),
        migrations.CreateModel(
            name='SalesPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sales_packages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HuntingPriceTypePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('price_list_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_price_type_package', to='bm_hunting_settings.huntingpricelisttype')),
                ('sales_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_price_type_package', to='bm_hunting_settings.salespackage')),
            ],
            options={
                'verbose_name_plural': 'Hunting Price Type Package',
                'db_table': 'hunting_price_type_package',
                'unique_together': {('price_list_type', 'sales_package')},
            },
        ),
    ]
