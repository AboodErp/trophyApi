# Generated by Django 4.2.9 on 2024-10-21 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_confirmation', '0003_salesconfirmationproposal_remarks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesconfirmationproposalitinerary',
            old_name='arrival_timezone',
            new_name='arrival_tz',
        ),
        migrations.RenameField(
            model_name='salesconfirmationproposalitinerary',
            old_name='departure_timezone',
            new_name='departure_tz',
        ),
    ]
