from django.db import models

class CategorieFilm(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    descriptif = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee_sortie = models.PositiveIntegerField()
    affiche = models.ImageField(upload_to='affiches/', )
    realisateur = models.CharField(max_length=100)
    categorie = models.ForeignKey(CategorieFilm, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre