# Generated by Django 4.1.4 on 2023-02-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0016_alter_booking_t_and_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='t_and_d',
            field=models.CharField(max_length=100, null=True),
        ),
    ]