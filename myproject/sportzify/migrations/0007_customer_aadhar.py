# Generated by Django 4.1.4 on 2023-01-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0006_alter_turf_turf_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='aadhar',
            field=models.IntegerField(max_length=12, null=True),
        ),
    ]