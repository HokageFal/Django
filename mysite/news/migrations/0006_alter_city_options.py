# Generated by Django 5.1 on 2024-09-01 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_city_alter_event_options_alter_myclubuser_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['title'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
    ]