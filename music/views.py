from django.shortcuts import render
from django.views.generic import DetailView

from music.models import Music
# Create your views here.


class MusicDetailView(DetailView):
    model = Music
    context_object_name = 'music'
    template_name = 'music/detail.html'
