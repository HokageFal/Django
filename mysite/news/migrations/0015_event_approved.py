# Generated by Django 5.1.1 on 2024-10-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_event_photo_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Опубликовать/одобрить'),
        ),
    ]
