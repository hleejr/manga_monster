import os, csv
from django.shortcuts import render
from django.http import HttpResponse
from manga_monster import settings

# Create your views here.
def index(request):

    with open(os.path.join(settings.BASE_DIR, 'manga', 'resources', 'manga_data.csv')) as f:
        reader = csv.reader(f)
        next(reader, None)
        manga = 0
        count = 0

        for row in reader:
            manga += 1    

    return HttpResponse('There are {} manga in this database'.format(manga), 200)