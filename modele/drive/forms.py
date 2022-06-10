from . import models
from django.forms import ModelForm
from .models import Categories, Client
from django import forms

class ClientForm(ModelForm):
    class Meta:
        model = models.Client
        fields = ('id','nom','prenom', 'date_inscription','adresse')
        labels = {
            'id' : 'idclient',
            'nom': 'nom',
            'prenom' : 'prenom',
            'date de inscription' : 'date_inscription' ,
            'adresse' : 'adresse',
        }


        localized_fields = ('date_inscription',)

class produits(models.Model):
   idproduit = models.CharsField(max_length=100)
   nom = models.CharField(max_length=100)
   date_peremption = models.DateField(blank=True, null=True)
   photos = models.models.ImageField(upload_to='static\image')
   marques = models.CharField(max_length=100)
   auteur = models.CharField(max_length=100)
   categorie = models.ForeignKey(idcate, on_delete=models.CASCADE, default=None)

   def __str__(self):
       return self.nom

   def dico(self):
       return {"idproduit": self.idproduit, "nom": self.nom, "date_peremption": self.date_peremption,
               "photos": self.photos, "marques": self.marques, "auteur": self.auteur, "categorie": self.categorie}


class commandes(models.Model):
   numcommande = models.CharsField(max_length=100)
   client = models.ForeignKey(idclient, on_delete=models.CASCADE, default=None)
   date = models.DateField(blank=True, null=True)

   def __str__(self):
       return self.client

   def dico(self):
       return {"numcommande": self.numcommande, "client": self.client, "date": self.date}


class listeproduits(models.Model):

  numcommande = models.ManytoManyField(numcommande, on_delete=models.CASCADE, default=None)
  quantite = models.CharField(max_length=100)
  idproduit = models.ManytoManyField(idproduit, on_delete=models.CASCADE, default=None)

  def __str__(self):
       return self.numcommande

  def dico(self):
      return {"numcommande": self.numcommande, "quantite": self.quantite, "idproduit": self.idproduit}








class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('id','nom','descriptif', 'date_inscription','adresse')
        labels = {
            'id': 'idcat',
            'nom' : 'nom',
            'descriptif' : 'descriptif',

        }


