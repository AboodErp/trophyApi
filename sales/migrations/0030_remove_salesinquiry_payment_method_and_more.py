# Generated by Django 4.2.9 on 2024-10-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0029_salesinquiry_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinquiry',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='salesinquiry',
            name='prev_experience',
        ),
    ]