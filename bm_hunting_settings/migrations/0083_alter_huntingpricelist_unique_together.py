# Generated by Django 4.2.9 on 2024-10-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0082_rename_huting_type_huntingpricelisttype_hunting_type_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='huntingpricelist',
            unique_together=set(),
        ),
    ]