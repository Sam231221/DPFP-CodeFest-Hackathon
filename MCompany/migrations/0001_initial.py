# Generated by Django 4.0.3 on 2022-04-24 14:50

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Company Name')),
                ('thumbnail', models.ImageField(help_text='Provide the image of your Company', null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator('mp4')])),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('slug', models.SlugField(editable=False, max_length=150, null=True, unique=True)),
                ('opening_time', models.DateTimeField(help_text='At what time your company starts?. Expected in AM', null=True)),
                ('closing_time', models.DateTimeField(help_text='At what time your company ends?. Expected in PM', null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('total_views', models.IntegerField(default=0)),
                ('phone_number', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1111111111), django.core.validators.MaxValueValidator(9999999999)])),
                ('user', models.OneToOneField(help_text='Owner of Company', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visitior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialtype', models.CharField(choices=[('Google', 'Google'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter')], max_length=50, null=True)),
                ('url', models.URLField(help_text='Provide the link of your any social link', null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCompany.company')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('working_hour', models.IntegerField(help_text='At what time your company starts?.', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sits', models.PositiveIntegerField(help_text='No of people enrolling for this service.', validators=[django.core.validators.MinValueValidator(1)])),
                ('bookmarks', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MCompany.company', verbose_name='Images')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('starting_time', models.DateTimeField(help_text='At what time your company starts?.', null=True)),
                ('ending_time', models.DateTimeField(help_text='At what time your company ends?.', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sits', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('bookmarks', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='views',
            field=models.ManyToManyField(blank=True, to='MCompany.visitior'),
        ),
    ]