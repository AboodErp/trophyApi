# Generated by Django 4.2.9 on 2024-10-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0013_alter_regulatoryhuntingpackage_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulatoryhuntingpackage',
            name='name',
            field=models.CharField(choices=[('Regular', 'Regular Safari'), ('Premium', 'Premium Safari'), ('Major', 'Major Safari')], max_length=100, unique=True),
        ),
    ]