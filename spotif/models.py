from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Premiacao(models.Model):
    nome = models.CharField(max_length=50)
    artista = models.ForeignKey(to=Artista, on_delete=models.CASCADE)

class Album(models.Model):
    generos=[
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("K-Pop", "K-Pop"),
        ("Pagode", "Pagode"),
        ("Samba", "Samba"),
        ("Sertanejo Universitário", "Sertanejo Universitário"),
        ("MPB", "MPB")
    ]
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50,choices=generos)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.artista.nome}"

class Musica(models.Model):
    titulo = models.CharField(max_length=50)
    compositor = models.CharField(max_length=50)
    gravadora = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True
                              , null=True)
    duracao = models.TimeField()

    def __str__(self):
        if (self.album is not None):
            return f"{self.titulo} - {self.album.titulo}"
        return f"{self.titulo} - Single"


class Playlist(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    musicas = models.ManyToManyField(Musica)
