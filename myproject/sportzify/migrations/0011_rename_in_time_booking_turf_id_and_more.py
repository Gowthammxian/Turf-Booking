# Generated by Django 4.1.4 on 2023-02-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0010_booking_date_booking_in_time_booking_out_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='in_time',
            new_name='turf_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='out_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='turf_uid',
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='uid',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
