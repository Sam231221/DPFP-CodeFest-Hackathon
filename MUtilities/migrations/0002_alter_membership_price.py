# Generated by Django 4.0.3 on 2022-04-24 15:17

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MUtilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, max_length=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
