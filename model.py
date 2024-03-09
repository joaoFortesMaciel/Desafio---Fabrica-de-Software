from django import models

class film(models.Model):
    # O título/Nome do filme.
    name = models.CharField(max_length=255)
    # A data de lançamento do filme.
    release_date = models.DateTimeField('')
    # O diretor do filme.
    director = models.CharField(max_length=255)
    # O protagonista do filme.
    protanogist = models.CharField(max_length=255)
    # O roteirista do filme.
    screenwriter = models.CharField(max_length=255)
    # O tempo de criação do objeto.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title