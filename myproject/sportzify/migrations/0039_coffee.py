# Generated by Django 4.1.4 on 2023-03-20 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0038_rename_review_reviewrating_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=1000)),
                ('paid', models.BooleanField(default=False)),
                ('turf_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportzify.turf')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sportzify.customer')),
            ],
        ),
    ]