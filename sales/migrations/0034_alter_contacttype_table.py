# Generated by Django 4.2.9 on 2024-10-10 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0033_alter_contacttype_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='contacttype',
            table='contact_types',
        ),
    ]