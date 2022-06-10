from django.db import models


class Client(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles
    idclient = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100 ,default = None)
    date_inscripion = models.DateField(blank=True, null=True)   # champs de type date, pouvant être null ou ne pas être rempli
    adresse = models.CharField(max_length=100)  # champs de type entier devant être obligatoirement rempli



    def __str__(self):
        chaine = str(f"Client {self.idcleint} {self.prenom} est inscris depuis le {self.date_inscripion} a  l'adresse {self.adresse}.")
        return chaine

    def dico(self):
        return {"Client": self.idclient, "nom": self.nom, "prenom": self.prenom, "date_inscripion": self.date_inscripion,
                "adresse": self.adresse}




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




class Categories(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles
    idcate = models.CharField(max_length=100)  # défini un champs de type texte de 100 caractères maximum
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)


    def __str__(self):
        chaine = str(f"Catégorie:  {self.idcate} nom de la catégorie {self.nom} descriptif : {self.descriptif}  ")
        return chaine

    def dico(self):
        return {"categorie": self.idcate, "nom_cat": self.nom, "descriptif": self.descriptif}





