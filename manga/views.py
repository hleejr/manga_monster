import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from manga_monster import settings
from .models import Manga, Readlist
from .forms import ReadlistCreateForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        readlists = self.get_queryset().filter(creator=request.user)
        return render(request, 'manga/readlists.html', {
          'readlists': readlists,
          'form': ReadlistCreateForm()
        })

    def post(self, request, userid, *args, **kwargs):
        form = ReadlistCreateForm(request.POST)

        if form.is_valid:
            Readlist = form.save(commit=False) # don't save the question yet
            Readlist.creator = request.user
            Readlist.save()
            form.save_m2m()
            
            return HttpResponseRedirect(
                reverse('user-readlist-page', args=[request.user.id]))
        # else if form is not valid
        return render(request, 'manga/readlists.html', { 'form': form })