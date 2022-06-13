from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


#CLIENT----------------------------------------------------------------
class clientform(ModelForm):
    class Meta:
        model = models.client
        fields = ('nom','prenom', 'date_inscription','adresse')
        labels = {
            'nom': _('Nom'),
            'prenom' : _('Prénom'),
            'adresse' : _('Adresse'),
        }

#Categorie-------------------------------------------------------------
class categorieform(ModelForm):
    class Meta:
        model = models.categorie
        fields = ('nom','descriptif')
        labels = {
            'nom' : _('Nom'),
            'descriptif' : _('Descriptif'),

        }

#PRODUITS--------------------------------------------------------------
class prduitsform(ModelForm):
    class Meta:
        model = models.produits
        fields = ('nom','date_peremption', 'photo','marque','auteur','categorie')
        labels = {
            'nom': _('Nom'),
            'date_peremption' : _('Date de péremption'),
            'photo' : _('Photo') ,
            'marque' : _('Marque'),
            'auteur': _('Auteur'),
            'categorie': _('categorie'),
        }

#COMMANDES---------------------------------------------------------------
class commandesform(ModelForm):
    class Meta:
        model = models.commande
        fields = ('numero_commande','client','date')
        labels = {
            'numero_commande' : _('Numéro de commande'),
            'client': _('Client'),
            'date' : _('Date'),
        }

#LISTEPRODUITS-------------------------------------------------------------
class listeproduitform(ModelForm):
    class Meta:
        model = models.listeproduit
        fields = ('commande','quantite','produit')
        labels = {
            'commandes' : _('Commande'),
            'quantite': _('Quantitée'),
            'produit' : _('Produit'),
        }