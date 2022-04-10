from django.urls import path

from playlist.views import PlaylistView

urlpatterns = [
    path('', PlaylistView.as_view(), name='playlist'),
]
