from distutils.command import upload
from wsgiref.handlers import format_date_time
from django.db import models


class Movie(models.Model):
    Genre = (
        ('comedy', 'comedy'),
        ('action', 'action'),
        ('drama', 'drama'),
    )
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    runtime = models.FloatField()
    year = models.DateField()
    genre = models.CharField(max_length=25, choices=Genre)
    description = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
