from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    album_title = models.CharField(max_length = 500)
    artist = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 1000)
    album_logo = models.CharField(max_length= 1000)

    def get_abolute_url(self):
        return reverse('musicapp:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default = False)

    def __str__(self):
        return self.album.artist + "-" + self.song_title
