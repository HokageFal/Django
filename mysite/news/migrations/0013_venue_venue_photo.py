# Generated by Django 5.1.1 on 2024-10-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_city_myclubuser_venue_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]