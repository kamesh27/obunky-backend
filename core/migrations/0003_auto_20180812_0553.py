# Generated by Django 2.0.7 on 2018-08-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180714_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='bhk',
            field=models.CharField(choices=[('IH', 'Independent House'), ('IA', 'Individual Apartment'), ('GS', 'Gated Society')], max_length=2),
        ),
        migrations.AlterField(
            model_name='flat',
            name='preferences',
            field=models.CharField(choices=[('A', 'No Alcohol'), ('S', 'No Smoking'), ('V', 'Vegetarian')], max_length=2),
        ),
    ]
