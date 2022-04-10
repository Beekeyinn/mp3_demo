from django.db import models

from accounts.models import User
from music.models import Music


# Create your models here.
class Playlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='playlists')
    musics = models.ManyToManyField(Music,blank=True, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self)->str:
        return str(self.user.username)

    class Meta:
        ordering = ('user',)