# Generated by Django 4.0.1 on 2022-01-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_property_areasqm_alter_property_rent'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='costPerSqm',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
