# Generated by Django 4.1.4 on 2023-01-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0005_alter_turf_cost_per_hr_alter_turf_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='turf_email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]