"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="app_accueil"),

    path('cours/', views.cours, name='app_cours'),
    path('cours/new', views.creer_cours, name='app_creer_cours'),
    path('cours/details/<int:cours_id>/', views.details_cours, name='app_details_cours'),

    path('account/login/', views.connexion, name='app_login'),
    path('account/signup/', views.inscription, name='app_signup'),
    
    path('profil/update/', views.mise_a_jour_profil, name='app_update_profil'),
    
    path('soumission/travail/<int:cours_id>/', views.soumettre_travail, name='app_soumettre_travail'),
    path('soumission/telechargement/fichier/<int:soumission_id>/', views.telecharger_fichier, name='app_telecharger_fichier'),
    path('soumission/autorisation/notation/<int:soumission_id>/', views.autoriser_et_noter_soumission, name='app_autoriser_et_noter_soumission'),

    path('tache/liste/', views.liste_taches, name='app_liste_taches'),
    path('tache/autoriser/', views.autoriser_tache, name='app_autoriser_tache'),
    path('tache/archivees/', views.liste_taches_archivees, name='app_liste_taches_archivees'),
    path('tache/<int:tache_id>/telecharger/', views.telecharger_fichier, name='app_telecharger_fichier'),
]
