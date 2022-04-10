from django.contrib import admin

from playlist.models import Playlist

# Register your models here.


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Playlist, PlaylistAdmin)
