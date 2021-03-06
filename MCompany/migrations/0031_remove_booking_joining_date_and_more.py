# Generated by Django 4.0.3 on 2022-04-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCompany', '0030_bookingplan_alter_booking_paying_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='joining_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='paying_plan',
        ),
        migrations.AddField(
            model_name='booking',
            name='availability',
            field=models.CharField(choices=[('Booked', 'Booked'), ('Book Now', 'Book Now')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='endinng_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6, max_length=4),
        ),
        migrations.AlterField(
            model_name='booking',
            name='starting_time',
            field=models.TimeField(null=True),
        ),
        migrations.DeleteModel(
            name='BookingPlan',
        ),
    ]
