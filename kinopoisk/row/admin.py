from django.contrib import admin

from .models import Actor, Genre, Movie, Reviews, MovieShots

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(MovieShots)
