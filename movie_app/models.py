from django.db import models
# from django.contrib.auth.models import User


class Movies(models.Model):
    # movie_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Title')
    release_date = models.DateField(auto_now=False, verbose_name='Release Date')
    genre = models.CharField(max_length=100, verbose_name='Genre')
    director = models.CharField(max_length=100, verbose_name='Director')

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'
        db_table = 'Movies'

    def __str__(self):
        return self.title
