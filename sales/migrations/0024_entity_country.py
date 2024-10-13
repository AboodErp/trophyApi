# Generated by Django 4.2.9 on 2024-10-09 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0041_alter_country_table'),
        ('sales', '0023_remove_entity_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bm_hunting_settings.country'),
        ),
    ]
