from django.urls import path
from . import views

urlpatterns = [
    #url clients
    path('', views.home),
    path('home/', views.home),
    path('ajout/', views.ajout),
    path("traitement/", views.traitement),
    path("affiche/<int:id>/", views.affiche),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update),
    path("traitementupdate/<int:id>", views.traitementupdate),
    #url categories

    #url
]