# Generated by Django 4.0.3 on 2022-04-28 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0012_rename_category_company_catego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='catego',
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MCompany.category'),
        ),
    ]