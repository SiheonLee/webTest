# Generated by Django 4.0.1 on 2022-01-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_property_costpersqm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='areaSqm',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='rent',
            field=models.IntegerField(default=1),
        ),
    ]