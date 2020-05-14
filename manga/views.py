import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from manga_monster import settings
from .models import Manga, Readlist
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class MangaListView(ListView):
    """ Renders a list of all manga """
    paginate_by = 75
    model = Manga

class MangaDetailView(DetailView):
    """ Renders a specific manga based on it's id"""
    model = Manga

    def get(self, request, id):
        """ Returns a specific manga page by id. """
        manga = self.get_queryset().get(id=id)
        return render(request, 'manga/manga.html', {
          'manga': manga,
          
        })

class ReadlistView(ListView):
    """ Renders a list of user's readlist """
    model = Readlist

    def get(self, request, userid):
        """ Returns a specific manga page by id. """
        readlists = self.get_queryset().get(creator=request.user)
        return render(request, 'manga/readlists.html', {
          'readlists': readlists,
     
        })