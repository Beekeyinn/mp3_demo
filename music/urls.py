from django.urls import path

from music.views import MusicDetailView

urlpatterns = [
    path(
        'detail/<int:pk>/', MusicDetailView.as_view(),
        name="music-detail"), ]
