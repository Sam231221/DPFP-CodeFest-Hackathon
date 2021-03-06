# Generated by Django 4.0.3 on 2022-04-24 16:10

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0002_alter_company_options_alter_company_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, max_length=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, max_length=4, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='event',
            name='ending_time',
            field=models.DateTimeField(help_text='At what time the event ends?.', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='starting_time',
            field=models.DateTimeField(help_text='At what time the event starts?.', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='working_hour',
            field=models.IntegerField(help_text='Mention in hour.', null=True),
        ),
    ]
