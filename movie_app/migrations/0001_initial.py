# Generated by Django 4.2.5 on 2023-10-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
                ('director', models.CharField(max_length=100, verbose_name='Director')),
            ],
            options={
                'verbose_name': 'Movies',
                'verbose_name_plural': 'Movies',
                'db_table': 'Movies',
            },
        ),
    ]
