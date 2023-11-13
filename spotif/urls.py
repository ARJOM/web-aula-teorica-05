from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_list, name="playlists"),
    path('detail/<int:id>', views.playlist_detail, name="playlist_detail"),
    # path('create/', PlaylistCreate.as_view(), name='playlist_creation')
    path('create/', views.playlist_create, name='playlist_creation')
]