from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    demographic = models.CharField(max_length=200)
    description = models.CharField(max_length=20000)
    link = models.CharField(max_length=200)
    img_link = models.CharField(default='', max_length=200)

    def __str__(self):
        return self.title

class Readlist(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    manga = models.ManyToManyField(Manga, through='ReadlistManga')

    def __str__(self):
        return self.name

class ReadlistManga(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.PROTECT)
    readlist = models.ForeignKey(Readlist, on_delete=models.PROTECT)
    