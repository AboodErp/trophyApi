# Generated by Django 4.2.9 on 2024-10-06 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0040_clientdocument_updated_at_clientdocument_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdocument',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_documents', to='hunter.client'),
        ),
    ]