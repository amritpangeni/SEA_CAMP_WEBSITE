# Generated by Django 3.2.9 on 2021-11-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webInterfaceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_sc', models.CharField(max_length=100)),
                ('title_1st', models.CharField(max_length=100)),
                ('title_2nd', models.CharField(max_length=100)),
                ('title_3rd', models.CharField(max_length=100)),
                ('title_4th', models.CharField(max_length=100)),
                ('event_venue_date', models.CharField(max_length=200)),
                ('video_link', models.CharField(max_length=200)),
                ('about_event', models.CharField(max_length=300)),
                ('where_event', models.CharField(max_length=300)),
                ('when_event_day', models.CharField(max_length=100)),
                ('when_event_date', models.CharField(max_length=100)),
                ('event_logo', models.ImageField(upload_to='uploads/')),
                ('venue', models.CharField(max_length=200)),
                ('venue_about', models.CharField(max_length=400)),
                ('background_top', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
