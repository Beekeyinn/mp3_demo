from django import template

from music.models import Music
from playlist.models import Playlist

register = template.Library()


@register.simple_tag
def is_in_playlist(request, id):
    music = Music.objects.get(id=id)
    playlist = Playlist.objects.filter(user=request.user).first()
    if playlist.musics.filter(id=music.id).exists():
        return True
    else:
        return False
