from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from music.models import Music
from .models import Playlist


# Create your views here.
class PlaylistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        playlist, created = Playlist.objects.get_or_create(user=user)
        context = {
            'playlist': playlist,
            'musics': playlist.musics.all(),
        }
        return render(
            request, 'playlist/playlist.html',
            context)

    def post(self, request, *args, **kwargs):
        playlist, created = Playlist.objects.get_or_create(
            user=request.user)
        try:
            music = Music.objects.get(
                id=request.POST.get('music_id', None))
        except Music.DoesNotExist:
            raise Http404("Music doesnot exist.")
        if playlist.musics.filter(id=music.id).exists():
            playlist.musics.remove(music)
            messages.success(
                request, "Music removed successfully from playlist.")
        else:
            playlist.musics.add(music)
            messages.success(request, "Music added to playlist")
        return redirect(reverse('playlist'))
