# Generated by Django 4.2.9 on 2024-10-08 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0049_alter_document_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]