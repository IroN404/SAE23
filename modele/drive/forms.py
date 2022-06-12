from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class clientform(ModelForm):
    class Meta:
        model = models.client
        fields = ('idclient','nom','prenom', 'date_inscription','adresse')
        labels = {
            'idclient' : 'idclient',
            'nom': 'nom',
            'prenom' : 'prenom',
            'date de inscription' : 'date_inscription' ,
            'adresse' : 'adresse',
        }


        localized_fields = ('date_inscription',)


class categoriesform(ModelForm):
    class Meta:
        model = models.categories
        fields = ('idcate','nom','descriptif', 'date_inscription','adresse')
        labels = {
            'idcate': 'idcate',
            'nom' : 'nom',
            'descriptif' : 'descriptif',

        }


class prduitsform(ModelForm):
    class Meta:
        model = models.produits
        fields = ('idproduit','nom','date_peremption', 'photos','marques','auteur','categories')
        labels = {
            'idproduit' : 'idclient',
            'nom': 'nom',
            'date_peremption' : 'date_peremption',
            'photos' : 'photos' ,
            'marques' : 'marques',
            'auteur': 'auteur',
            'categories': 'categories'
        }

class commandes(ModelForm):
    class Meta:
        model = models.produits
        fields = ('numcommande','client','date', 'photos','marques','auteur','categories')
        labels = {
            'numcommande' : 'numcommande',
            'client': 'client',
            'date' : 'date'
        }

class listeproduitsform(ModelForm):
    class Meta:
        model = models.listeproduits
        fields = ('commande','quantite','produit')
        labels = {
            'commande' : 'commande',
            'quantite': 'quantite',
            'produit' : 'produit'
        }