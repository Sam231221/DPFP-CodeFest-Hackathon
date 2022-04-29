# Generated by Django 4.0.3 on 2022-04-28 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MCompany', '0008_company_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ordered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usereventorders', to=settings.AUTH_USER_MODEL),
        ),
    ]
