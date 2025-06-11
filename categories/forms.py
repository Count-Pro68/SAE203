from django import forms
from .models import CategorieFilm

class CategorieFilmForm(forms.ModelForm):
    class Meta:
        model = CategorieFilm
        fields = ['nom']