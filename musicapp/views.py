from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views import generic
from django.http import Http404, HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = 'musicapp/index.html'
    context_object_name = 'all_album'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DeleteView):
    model = Album
    template_name = 'musicapp/detail.html'

'''
def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album' : all_album,
    }
    return render(request, "musicapp/index.html", context)
'''
#    all_album = Album.objects.all()
#    template = loader.get_template('musicapp/index.html')
#    context = {
#        'all_album' : all_album,
#    }
#    return HttpResponse(template.render(context, request))
'''

def detail(request, album_id):
    try:
        album = Album.objects.get(id = album_id)
    except Album.DoesNotExist:
        raise Http404("틀렸어 병신아")
    context = {
        'album' : album,
    }
    return render(request, "musicapp/detail.html", context)
'''

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


def favorite(request, album_id):
    album = get_object_or_404(Album, pk = album_id)
    try:
        select_song=album.song_set.get(pk = request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'musicapp/detail.html', {
                      'album' : album,
                      'error_message' : "Yiu did not select a valid song."
        })
    else:
        select_song.is_favorite = True
        select_song.save()
    return render(request, 'musicapp/detail.html', {'album':album})