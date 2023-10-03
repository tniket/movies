from django.contrib import admin
from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'genre', 'director']


admin.site.register(Movies, MoviesAdmin)

