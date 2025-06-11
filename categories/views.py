from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import CategorieFilm
from .forms import CategorieFilmForm

def liste_categories(request):
    categories = CategorieFilm.objects.all()
    return render(request, 'categories/liste.html', {'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieFilmForm()
    return render(request, 'categories/formulaire.html', {'form': form, 'titre': 'Ajouter une catégorie'})

def modifier_categorie(request, id):
    categorie = get_object_or_404(CategorieFilm, pk=id)
    if request.method == 'POST':
        form = CategorieFilmForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieFilmForm(instance=categorie)
    return render(request, 'categories/formulaire.html', {'form': form, 'titre': 'Modifier la catégorie'})

def supprimer_categorie(request, id):
    categorie = get_object_or_404(CategorieFilm, pk=id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'categories/supprimer.html', {'categorie': categorie})