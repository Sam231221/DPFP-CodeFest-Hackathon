# Generated by Django 4.0.3 on 2022-04-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0023_category_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
        migrations.AddField(
            model_name='gymplan',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, max_length=4, null=True),
        ),
    ]
