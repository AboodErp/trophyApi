# Generated by Django 4.2.9 on 2024-10-28 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bm_hunting_settings', '0008_alter_regulatoryhuntingpackagespecies_r_hunting_package_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HuntingPackageCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customized_area_set', to='bm_hunting_settings.huntingarea')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customization', to='bm_hunting_settings.currency')),
                ('hunting_price_list_type_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customization', to='bm_hunting_settings.huntingpricetypepackage')),
                ('hunting_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customized_hunting_type_set', to='bm_hunting_settings.huntingtype')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customized_season_set', to='bm_hunting_settings.seasons')),
            ],
            options={
                'verbose_name_plural': 'Hunting Package Customization',
                'db_table': 'sales_package_customization',
            },
        ),
        migrations.CreateModel(
            name='HuntingPackageCustomizedSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('hunting_package_customization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customized_set', to='bm_hunting_settings.huntingpackagecustomization')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunting_package_customized_species_set', to='bm_hunting_settings.species')),
            ],
            options={
                'verbose_name_plural': 'Hunting Package Customized Species',
                'db_table': 'hunting_package_customized_species',
            },
        ),
    ]