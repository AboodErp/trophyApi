# Generated by Django 5.0.4 on 2024-10-03 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0006_packagetype_trophyfees_salespackagehuntingspecies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='package_name',
        ),
    ]