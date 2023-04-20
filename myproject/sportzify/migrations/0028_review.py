# Generated by Django 4.1.4 on 2023-03-13 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0027_timeslot_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200, null=True)),
                ('rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('turf_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportzify.turf')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportzify.customer')),
            ],
        ),
    ]
