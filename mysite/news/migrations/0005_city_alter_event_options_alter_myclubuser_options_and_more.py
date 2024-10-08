# Generated by Django 5.1 on 2024-09-01 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_myclubuser_venue_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=120)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_date'], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='myclubuser',
            options={'ordering': ['first_name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ['-name'], 'verbose_name': 'Место проведения'},
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.city'),
        ),
    ]
