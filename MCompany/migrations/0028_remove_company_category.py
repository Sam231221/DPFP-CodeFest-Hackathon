# Generated by Django 4.0.3 on 2022-04-29 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0027_alter_company_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='category',
        ),
    ]