from django.urls import path
from . import views

urlpatterns = [
    path('', views.MangaListView.as_view(), name='index'),
    path('manga/<int:id>/', views.MangaDetailView.as_view(), name='manga-details-page'),
    path('readlists/<int:userid>/', views.ReadlistView.as_view(), name='user-readlist-page'),

]