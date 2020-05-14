import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from manga_monster import settings
from .models import Manga
from django.views.generic.list import ListView

# Create your views here.
class MangaListView(ListView):
    """ Renders a list of all Pages. """
    model = Manga

    def get(self, request):
        """ GET a list of Pages. """
        manga = self.get_queryset().all()
        return render(request, 'manga/index.html', {
          'manga': manga
        })