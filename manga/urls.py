from django.urls import path
from . import views

urlpatterns = [
    path('', views.MangaListView.as_view(), name='index')
]