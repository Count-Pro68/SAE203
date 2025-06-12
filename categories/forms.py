from django import forms
from .models import CategorieFilm
from .models import Film

class CategorieFilmForm(forms.ModelForm):
    class Meta:
        model = CategorieFilm
        fields = ['nom', 'descriptif']

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['titre', 'annee_sortie', 'affiche', 'realisateur', 'categorie']
