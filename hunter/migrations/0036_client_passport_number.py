# Generated by Django 5.0.4 on 2024-10-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0035_remove_client_client_type_client_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='passport_number',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]