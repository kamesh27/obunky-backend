# Generated by Django 2.0.7 on 2018-08-12 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180812_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='posted_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
