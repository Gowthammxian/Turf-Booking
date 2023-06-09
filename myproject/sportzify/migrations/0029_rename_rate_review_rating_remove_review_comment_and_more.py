# Generated by Django 4.1.4 on 2023-03-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportzify', '0028_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rate',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
