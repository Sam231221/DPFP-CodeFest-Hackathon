# Generated by Django 4.0.3 on 2022-04-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0035_alter_booking_options_alter_booking_ending_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ending_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='starting_time',
            field=models.TimeField(null=True),
        ),
    ]
