# Generated by Django 4.2.9 on 2024-10-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter', '0050_delete_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapontype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Weapon Types',
                'db_table': 'weapon_type',
            },
        ),
    ]