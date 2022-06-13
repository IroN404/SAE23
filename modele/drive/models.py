from django.db import models



class categories(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles  # défini un champs de type texte de 100 caractères maximum
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)


    def __str__(self):
        chaine = str(f"Catégorie:  {self.idcate} nom de la catégorie {self.nom} descriptif : {self.descriptif}  ")
        return chaine

    def dico(self):
        return {"categorie": self.idcate, "nom_cat": self.nom, "descriptif": self.descriptif}


class client(models.Model):  # déclare la classe Lieu héritant de la classe Model, classe de base des modèles  # défini un champs de type texte de 100 caractères maximum
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100 ,default = None)
    date_inscription = models.DateField(blank=True, null=True)   # champs de type date, pouvant être null ou ne pas être rempli
    adresse = models.CharField(max_length=100)  # champs de type entier devant être obligatoirement rempli



    def __str__(self):
        chaine = str(f"Client {self.nom} {self.prenom} est inscris depuis le {self.date_inscription} a  l'adresse {self.adresse}.")
        return chaine

    def dico(self):
        return { "nom": self.nom, "prenom": self.prenom, "date_inscription": self.date_inscription,"adresse": self.adresse}




class produits(models.Model):
   idproduit = models.CharField(max_length=100)
   nom = models.CharField(max_length=100)
   date_peremption = models.DateField(blank=True, null=True)
   photos = models.CharField(max_length=100)
   marques = models.CharField(max_length=100)
   auteur = models.CharField(max_length=100)
   categories = models.ForeignKey("categories", on_delete=models.CASCADE, default=None)

   def __str__(self):
       return self.nom

   def dico(self):
       return {"idproduit": self.idproduit, "nom": self.nom, "date_peremption": self.date_peremption, "photos": self.photos, "marques": self.marques, "auteur": self.auteur, "categorie": self.categorie}


class commandes(models.Model):
   numcommande = models.CharField(max_length=100)
   client = models.ForeignKey("client", on_delete=models.CASCADE, default=None)
   date = models.DateField(blank=True, null=True)

   def __str__(self):
       return self.client

   def dico(self):
       return {"numcommande": self.numcommande, "client": self.client, "date": self.date}



class listeproduits(models.Model):

  commandes = models.ForeignKey("commandes", on_delete=models.CASCADE, default=None)
  quantite = models.CharField(max_length=100)
  produits = models.ForeignKey("produits", on_delete=models.CASCADE, default=None)

  def __str__(self):
       return self.commandes

  def dico(self):
      return {"commandes": self.commandes, "quantite": self.quantite, "produits": self.produits}

