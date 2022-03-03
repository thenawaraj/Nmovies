from distutils.command import upload
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    Genre = (
        ('comedy', 'comedy'),
        ('action', 'action'),
        ('drama', 'drama'),
    )
    title = models.CharField(max_length=100)
    rating = models.FloatField(max_digits=1)
    runtime =models.FloatField()
    year = models.DateField()
    genre = models.CharField(max_length=25, choices=Genre)
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
