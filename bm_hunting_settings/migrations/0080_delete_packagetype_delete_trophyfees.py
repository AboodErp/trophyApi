# Generated by Django 4.2.9 on 2024-10-16 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0079_rename_amont_huntingpackagecompanionshunter_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PackageType',
        ),
        migrations.DeleteModel(
            name='TrophyFees',
        ),
    ]
