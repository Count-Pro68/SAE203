from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_categories, name='liste_categories'),
    #path('<int:pk>/', views.detail_categorie, name='detail_categorie'),
    path('ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('<int:pk>/modifier/', views.modifier_categorie, name='modifier_categorie'),
    path('<int:pk>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),

    # Films liés à une catégorie
    path('<int:pk>/films/', views.films_par_categorie, name='films_par_categorie'),
    path('films/<int:pk>/modifier/', views.modifier_film, name='modifier_film'),
    path('films/<int:pk>/supprimer/', views.supprimer_film, name='supprimer_film'),
]
