# Generated by Django 4.2.9 on 2024-10-26 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_confirmation', '0011_alter_salesconfirmationproposalstatus_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesconfirmationproposalstatus',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_confirmation_status_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
