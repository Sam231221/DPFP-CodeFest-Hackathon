# Generated by Django 4.0.3 on 2022-04-29 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0028_remove_company_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCompany.category'),
        ),
    ]
