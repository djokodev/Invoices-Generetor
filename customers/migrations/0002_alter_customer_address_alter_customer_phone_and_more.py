# Generated by Django 5.1.3 on 2024-12-03 03:45

import customers.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(max_length=20, validators=[customers.validators.validate_postal_code]),
        ),
    ]
