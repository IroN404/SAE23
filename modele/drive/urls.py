from django.urls import path
from . import views

urlpatterns = [
    #URL produits
    path('', views.home, name='home'),
    path('ajout/<int:id>/', views.ajout, name=('ajout')),
    path('traitement/<int:id>/', views.traitement, name=('traitement')),
    path('infos/', views.infos, name=('infos_produits')),
    path('affiche_/<int:id>/', views.affiche, name=('affiche')),
    path('update/<int:id>/', views.update, name=('update')),
    path('updatetraitement/<int:id>/', views.updatetraitement, name=('updatetraitement')),
    path('delete/<int:id>/', views.delete, name=('delete')),
    #URL catégorie
    #URL clients
    #URL commandes
]