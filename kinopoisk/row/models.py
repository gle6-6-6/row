from datetime import date

from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField('Имя', max_length=60)
    url = models.SlugField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Actor(models.Model):
    name = models.CharField('Имя', max_length=80)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    image = models.ImageField('Изображение', upload_to='actors')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'


class Movie(models.Model):
    title = models.CharField('Название', max_length=60)
    slogan = models.CharField('Слоган', max_length=90)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to="movies")
    directors = models.ManyToManyField(Actor, verbose_name='Режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='film_actor')
    genre = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0)
    sbor = models.PositiveIntegerField('Сборы', default=0)
    url = models.SlugField(max_length=120)
    country = models.CharField('Страна', max_length=50, default="")

    def get_absolute_url(self):
        return reverse('movie_about', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, )
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"
