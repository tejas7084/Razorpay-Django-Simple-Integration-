# Generated by Django 2.0.2 on 2021-01-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razor', '0002_auto_20210129_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='razorpay',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
