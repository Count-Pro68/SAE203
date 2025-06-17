from django.shortcuts import render, redirect, get_object_or_404
from .models import CategorieFilm, Film
from .forms import CategorieFilmForm, FilmForm

#------------- CRUD CategorieFilm --------------#

def liste_categories(request):
    categories = CategorieFilm.objects.all()
    return render(request, 'categories/liste.html', {'categories': categories})

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieFilmForm(request.POST)
        if form.is_valid():
            categorie = form.save()
            return redirect('films_par_categorie', pk=categorie.id)
    else:
        form = CategorieFilmForm()
    return render(request, 'categories/formulaire.html', {'form': form, 'titre': 'Ajouter une catégorie'})

def modifier_categorie(request, pk):
    categorie = get_object_or_404(CategorieFilm, pk=pk)
    if request.method == 'POST':
        form = CategorieFilmForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('films_par_categorie', pk=categorie.id)
    else:
        form = CategorieFilmForm(instance=categorie)
    return render(request, 'categories/formulaire.html', {'form': form, 'titre': 'Modifier la catégorie'})

def supprimer_categorie(request, pk):
    categorie = get_object_or_404(CategorieFilm, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'categories/supprimer.html', {'categorie': categorie})

# Affiche les films d'une catégorie avec ajout possible

def films_par_categorie(request, pk):
    categorie = get_object_or_404(CategorieFilm, pk=pk)
    films = Film.objects.filter(categorie=categorie)

    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.categorie = categorie
            film.save()
            return redirect('films_par_categorie', pk=categorie.pk)
    else:
        form = FilmForm()

    return render(request, 'categories/films_par_categorie.html', {
        'categorie': categorie,
        'films': films,
        'form': form,
        'titre': f"Films dans la catégorie : {categorie.nom}"
    })

#-------------- CRUD Film hors catégorie (liste générale) --------------#

def liste_films(request):
    films = Film.objects.all()
    return render(request, 'films/liste.html', {'films': films})

def ajouter_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('liste_films')
    return render(request, 'films/formulaire.html', {'form': form, 'titre': 'Ajouter un film'})

def modifier_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('films_par_categorie', pk=film.categorie.pk)
    else:
        form = FilmForm(instance=film)
    return render(request, 'categories/film_form.html', {
        'form': form,
        'titre': f'Modifier le film : {film.titre}'
    })

def supprimer_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    categorie_id = film.categorie.pk
    if request.method == 'POST':
        film.delete()
        return redirect('films_par_categorie', pk=categorie_id)
    return render(request, 'films/supprimer.html', {'film': film})