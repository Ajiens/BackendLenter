# Generated by Django 5.0 on 2024-01-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('cover_link', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('rating_count', models.IntegerField(blank=True, null=True)),
                ('review_count', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.FloatField(blank=True, null=True)),
                ('five_star_ratings', models.IntegerField(blank=True, null=True)),
                ('four_star_ratings', models.IntegerField(blank=True, null=True)),
                ('three_star_ratings', models.IntegerField(blank=True, null=True)),
                ('two_star_ratings', models.IntegerField(blank=True, null=True)),
                ('one_star_ratings', models.IntegerField(blank=True, null=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('date_published', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('isbn', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('genre', models.JSONField()),
            ],
        ),
    ]
