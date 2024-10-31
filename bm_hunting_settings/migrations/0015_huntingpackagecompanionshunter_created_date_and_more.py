# Generated by Django 5.1.2 on 2024-10-31 09:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0014_alter_regulatoryhuntingpackage_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='huntingpackagecompanionshunter',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='huntingpackagecompanionshunter',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='huntingpackagecompanionshunter',
            unique_together={('hunting_price_list_type_package', 'days')},
        ),
    ]