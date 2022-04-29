# Generated by Django 4.0.3 on 2022-04-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0015_event_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='email',
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Business Email'),
        ),
    ]
