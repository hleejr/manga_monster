import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from manga_monster import settings
from .models import Manga
# Create your views here.
def index(request): 
    context = {
        'manga': Manga.objects.all()
    }
    return render(request, 'manga/index.html', context)