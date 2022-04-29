# Generated by Django 4.0.3 on 2022-04-24 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0003_event_price_service_price_alter_event_ending_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCompany.company'),
        ),
        migrations.AddField(
            model_name='service',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCompany.company'),
        ),
    ]
