# Generated by Django 4.1.4 on 2023-01-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0004_turf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='cost_per_hr',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='turf',
            name='turf_phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
