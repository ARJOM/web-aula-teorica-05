from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from spotif.forms import PlaylistForm
from spotif.models import Playlist, Musica


def playlist_list(request):
    playlist = Playlist.objects.all()
    return render(request, 'playlists.html', {'items': playlist})


def playlist_detail(request, id):
    playlist = Playlist.objects.get(id=id)
    return render(request, 'playlist.html', {'item': playlist})


def playlist_create(request):
    context = {}
    musicas = Musica.objects.all()
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            object = form.save()
            musics = []
            for musica in musicas:
                music_id = request.POST.get(musica.titulo)
                if music_id is not None:
                    music_object = Musica.objects.get(id=music_id)
                    music_object.save()
                    musics.append(music_object)
            object.musicas.set(musics)
            return redirect('playlists')

    context['form'] = PlaylistForm()
    context['musicas'] = musicas
    return render(request, 'form.html', context)

# class PlaylistCreate(CreateView):
#     model = Playlist
#     template_name = 'form.html'
#     fields = ('nome', 'descricao')
#     success_url = reverse_lazy('playlists')
#     musicas = []
#
#     def get_context_data(self, **kwargs):
#         kwargs['musicas'] = Musica.objects.all()
#         return super(PlaylistCreate, self).get_context_data(**kwargs)
#
#     def post(self, request, *args, **kwargs):
#         print(self.request.POST)
#         musics = []
#         for musica in Musica.objects.all():
#             music_id = self.request.POST.get(musica.titulo)
#             if music_id is not None:
#                 music_object = Musica.objects.get(id=music_id)
#                 print(music_object)
#                 music_object.save()
#                 musics.append(music_object)
#         self.musicas = musics
#         return super(PlaylistCreate, self).post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.musicas.set(self.musicas)
#         return HttpResponseRedirect(self.get_success_url())