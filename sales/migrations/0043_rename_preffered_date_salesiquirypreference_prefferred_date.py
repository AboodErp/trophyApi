# Generated by Django 4.2.9 on 2024-10-13 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0042_alter_contacttype_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesiquirypreference',
            old_name='preffered_date',
            new_name='prefferred_date',
        ),
    ]