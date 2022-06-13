from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class clientform(ModelForm):
    class Meta:
        model = models.client
        fields = ('nom','prenom', 'date_inscription','adresse')
        labels = {
            'nom': 'nom',
            'prenom' : 'prenom',
            'date_inscription' : 'date de inscription' ,
            'adresse' : 'adresse',
        }


        localized_fields = ('date_inscription',)


class categoriesform(ModelForm):
    class Meta:
        model = models.categories
        fields = ('nom','descriptif')
        labels = {
            'nom' : 'nom',
            'descriptif' : 'descriptif',

        }


class prduitsform(ModelForm):
    class Meta:
        model = models.produits
        fields = ('idproduit','nom','date_peremption', 'photos','marques','auteur','categories')
        labels = {
            'idproduit' : 'idproduit',
            'nom': 'nom',
            'date_peremption' : 'date de peremption',
            'photos' : 'photos' ,
            'marques' : 'marques',
            'auteur': 'auteur',
            'categories': 'categories'
        }

class commandesform(ModelForm):
    class Meta:
        model = models.commandes
        fields = ('numcommande','client','date')
        labels = {
            'numcommande' : 'numcommande',
            'client': 'client',
            'date' : 'date'
        }

class listeproduitsform(ModelForm):
    class Meta:
        model = models.listeproduits
        fields = ('commandes','quantite','produits')
        labels = {
            'commandes' : 'commande',
            'quantite': 'quantite',
            'produits' : 'produit'
        }