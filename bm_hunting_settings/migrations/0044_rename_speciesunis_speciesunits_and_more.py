# Generated by Django 4.2.9 on 2024-10-10 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0043_accommodationtype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpeciesUnis',
            new_name='SpeciesUnits',
        ),
        migrations.AlterModelTable(
            name='speciesunits',
            table=None,
        ),
    ]