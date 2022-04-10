from django.contrib import admin

from music.models import Genre, Music

# Register your models here.

class MusicInline(admin.StackedInline):
    model = Music
    extra=1

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [MusicInline,]

admin.site.register(Genre, GenreAdmin)




class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'singer', 'active']


admin.site.register(Music, MusicAdmin)
