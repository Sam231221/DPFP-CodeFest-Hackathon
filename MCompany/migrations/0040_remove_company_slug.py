# Generated by Django 4.0.3 on 2022-04-29 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0039_alter_booking_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
    ]