# Enter in shell after running command python manage.py shell from root directory

import os, csv
from manga.models import Manga
from manga_monster import settings

def import_csv():

    with open(os.path.join(settings.BASE_DIR, 'manga', 'resources', 'manga_data.csv')) as f:
        reader = csv.reader(f)
        next(reader, None)
        count = 0 

        for row in reader:
            count += 1

            if count <= 20:
                 _, created = Manga.objects.get_or_create(title = row[4],author = row[5],artist = row[6],genre = row[8],demographic = row[9],description = row[7],link = row[3])

            if count >= 21:
                 _, created = Manga.objects.get_or_create(title = row[4],author = row[5],artist = row[6],genre = row[7],demographic = row[8],description = row[9],link = row[3])
    
    return Manga.objects.all()

import_csv()