# Generated by Django 2.0.7 on 2018-07-14 03:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='photo_urls',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1024), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='flat',
            name='property_type',
            field=models.CharField(choices=[('IH', 'Independent House'), ('IA', 'Individual Apartment'), ('GS', 'Gated Society')], max_length=5),
        ),
    ]
