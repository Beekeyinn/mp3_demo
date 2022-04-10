from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from music.models import Music


class IndexView(ListView):
    template_name = "index.html"
    paginate_by = 10
    context_object_name = 'music'

    def get_queryset(self, *args, **kwargs):
        return Music.objects.all()


class SearchView(ListView):
    template_name = 'search.html'
    paginate_by = 5

    def get_queryset(self, * args, **kwargs):
        query = self.request.GET.get('query')
        lookups = (
            Q(title__icontains=query) |
            Q(singer__icontains=query) |
            Q(genre__name__icontains=query)
        )
        music = Music.objects.filter(lookups).distinct()
        return music
