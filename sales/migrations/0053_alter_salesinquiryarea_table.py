# Generated by Django 4.2.9 on 2024-10-15 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0052_alter_salesinquiryarea_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='salesinquiryarea',
            table='sales_inquiry_areas',
        ),
    ]