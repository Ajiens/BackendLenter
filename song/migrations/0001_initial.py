# Generated by Django 5.0 on 2024-01-21 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('artist', models.CharField(max_length=128)),
                ('audio_file', models.FileField(upload_to='song/')),
                ('cover_image', models.FileField(blank=True, upload_to='cover/')),
                ('cover_link', models.TextField(blank=True)),
                ('audio_length_string', models.CharField(max_length=64)),
                ('audio_length_second', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
