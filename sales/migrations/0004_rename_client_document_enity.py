# Generated by Django 4.2.9 on 2024-10-25 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_contacts_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='client',
            new_name='enity',
        ),
    ]
