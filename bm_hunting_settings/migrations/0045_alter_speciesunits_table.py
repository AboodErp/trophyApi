# Generated by Django 4.2.9 on 2024-10-10 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0044_rename_speciesunis_speciesunits_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='speciesunits',
            table='species_units',
        ),
    ]