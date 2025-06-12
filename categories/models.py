from django.db import models



class CategorieFilm(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    descriptif = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.nom