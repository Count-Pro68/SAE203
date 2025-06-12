from django.shortcuts import render, redirect, get_object_or_404
from .models import CategorieFilm
from .forms import CategorieFilmForm, FilmForm

#--------- CRUD CategorieFilm ---------#


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


#--------- CRUD Film ---------#


# Liste des films
def liste_films(request):
    films = Film.objects.all()
    return render(request, 'categories/films/liste.html', {'films': films})

# Ajouter un film
def ajouter_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('liste_films')
    return render(request, 'categories/films/formulaire.html', {'form': form, 'titre': 'Ajouter un film'})

# Modifier un film
def modifier_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)
    if form.is_valid():
        form.save()
        return redirect('liste_films')
    return render(request, 'categories/films/formulaire.html', {'form': form, 'titre': 'Modifier le film'})

# Supprimer un film
def supprimer_film(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    if request.method == 'POST':
        film.delete()
        return redirect('liste_films')
    return render(request, 'categories/films/supprimer.html', {'film': film})
