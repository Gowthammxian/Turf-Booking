# Generated by Django 4.1.4 on 2023-03-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0036_remove_reviewrating_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.IntegerField(),
        ),
    ]