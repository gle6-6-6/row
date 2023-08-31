# Generated by Django 4.2.4 on 2023-08-09 13:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('image', models.ImageField(upload_to='actors', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Актеры и режиссеры',
                'verbose_name_plural': 'Актеры и режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('url', models.SlugField(max_length=120)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Название')),
                ('slogan', models.CharField(max_length=90, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movies', verbose_name='Постер')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Примьера в мире')),
                ('url', models.SlugField(max_length=120)),
                ('actors', models.ManyToManyField(related_name='film_actor', to='row.actor', verbose_name='Актеры')),
                ('directors', models.ManyToManyField(related_name='film_director', to='row.actor', verbose_name='Режиссер')),
                ('genre', models.ManyToManyField(to='row.genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='row.movie', verbose_name='фильм')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]