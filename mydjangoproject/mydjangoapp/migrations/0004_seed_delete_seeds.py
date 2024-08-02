# Generated by Django 4.1.13 on 2024-07-19 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mydjangoapp', '0003_equipmentstatus_restrictedarea_securitybreach_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeedID', models.CharField(max_length=100)),
                ('SeedCategory', models.CharField(max_length=255)),
                ('SeedType', models.CharField(max_length=255)),
                ('DateBought', models.DateTimeField(default=django.utils.timezone.now)),
                ('ExpiryDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('PlantingDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('TemperatureRequirement', models.FloatField()),
                ('LightRequirement', models.FloatField()),
                ('MoistureRequirement', models.FloatField()),
                ('SeedQuantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='seeds',
        ),
    ]