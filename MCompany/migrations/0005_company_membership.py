# Generated by Django 4.0.3 on 2022-04-25 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MUtilities', '0004_remove_membership_company_and_more'),
        ('MCompany', '0004_event_company_service_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MUtilities.membership'),
        ),
    ]
