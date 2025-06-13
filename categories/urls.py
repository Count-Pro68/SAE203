from django.urls import path
from . import views

urlpatterns = [

    # Categorie
    path('', views.liste_categories, name='liste_categories'),
    path('ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),

    # lien
    path('categorie/<int:categorie_id>/', views.detail_categorie, name='detail_categorie'),

    # Films
    path('films/', views.liste_films, name='liste_films'),
    path('films/ajouter/', views.ajouter_film, name='ajouter_film'),
    path('films/modifier/<int:film_id>/', views.modifier_film, name='modifier_film'),
    path('films/supprimer/<int:film_id>/', views.supprimer_film, name='supprimer_film'),
]