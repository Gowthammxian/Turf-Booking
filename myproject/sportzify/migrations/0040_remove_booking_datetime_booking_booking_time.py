# Generated by Django 4.1.4 on 2023-04-19 09:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0039_coffee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='datetime',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
