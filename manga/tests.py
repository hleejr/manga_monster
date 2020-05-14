from django.test import TestCase
from django.contrib.auth.models import User
from manga.models import Manga, Readlist, ReadlistManga


# Create your tests here.
class MangaTest(TestCase):

    def test_get(self):
        user = User.objects.create_user(username='admin', password='djangopony')
        self.client.login(username='admin', password='djangopony')

        manga = Manga.objects.create(title = 'Nani?!',author = 'Nani?!',artist = 'Nani?!',genre = 'Nani?!',demographic = 'Nani?!',description = 'Nani?!',link = 'Nani?!', img_link = 'Nani?!')
        manga.save()

        response = self.client.get('/manga/%d/' % manga.id)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nani?!')

class ReadlistTest(TestCase):

    def test_create(self):
        user = User.objects.create_user(username='admin', password='djangopony')
        self.client.login(username='admin', password='djangopony')

        manga = Manga.objects.create(title = 'Nani?!',author = 'Nani?!',artist = 'Nani?!',genre = 'Nani?!',demographic = 'Nani?!',description = 'Nani?!',link = 'Nani?!', img_link = 'Nani?!')
        manga.save()

        new = {
            'csrfmiddlewaretoken': '7lMq3HQrhWdtW5xS6VKf2alTLFAmvn2liZRz2PdeQAL5NnMGJ1KQTLpIfamBa8BN',
            'name': 'testing title',
            'manga': [ manga.id ]
        }

        response = self.client.post('/readlists/%d/' % user.id, new)
        updated = Readlist.objects.get(name = new['name'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated.name, new['name'])