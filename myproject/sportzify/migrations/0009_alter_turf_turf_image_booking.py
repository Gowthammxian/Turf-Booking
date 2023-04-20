# Generated by Django 4.1.4 on 2023-01-31 08:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0008_alter_turf_turf_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turf',
            name='turf_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_uid', models.UUIDField(default=uuid.uuid4)),
                ('t_and_d', models.DateTimeField()),
                ('turf_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportzify.turf')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sportzify.customer')),
            ],
        ),
    ]
