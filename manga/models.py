from django.db import models

# Create your models here.

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    demographic = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title