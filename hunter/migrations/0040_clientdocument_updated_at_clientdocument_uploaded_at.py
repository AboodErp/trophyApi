# Generated by Django 5.0.4 on 2024-10-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0039_remove_client_passport_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdocument',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='clientdocument',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]