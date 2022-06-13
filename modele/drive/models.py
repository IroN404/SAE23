from django.db import models


#CATEGORIE----------------------------------------------------------------
class categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom": self.nom, "descriptif": self.descriptif}


#PRODUITS----------------------------------------------------------------
class produits(models.Model):
    nom = models.CharField(max_length=100)
    date_peremption = models.DateField(blank=True, null=True)
    photos = models.ImageField(upload_to ='/media/')
    marques = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categories = models.ForeignKey("categories", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom} de {self.marques}, périme le {self.date_peremption}. Catégorie : {self.categories}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "date_peremption": self.date_peremption, "photos": self.photos, "marques": self.marques, "auteur": self.auteur, "categorie": self.categorie}

#CLIENTS------------------------------------------------------------------
class client(models.Model):
    numero_client = models.IntegerField(blank=True, null=True)
    nom = models.CharField(max_length=20,blank=False)
    prenom = models.CharField(max_length=20 ,blank=False)
    date_inscription = models.DateField(blank=False, null=True)
    adresse = models.CharField(max_length=40)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom}, client n°{self.numero_client} est inscris depuis le {self.date_inscription} à l'adresse {self.adresse}."
        return chaine

    def dico(self):
        return {"numero_client":self.numero_client, "nom": self.nom, "prenom": self.prenom, "date_inscription": self.date_inscription,"adresse": self.adresse}

#COMMANDE----------------------------------------------------------------
class commande(models.Model):
    numero_commande = models.CharField(max_length=100)
    client = models.ForeignKey("client", on_delete=models.CASCADE, default=None)
    date = models.DateField(blank=False, null=True)

    def __str__(self):
        chaine = f"commande n°{self.numero_commande}, du client {self.client}, effectuée le {self.date}"
        return chaine

    def dico(self):
        return {"numero_commande": self.numero_commande, "client": self.client, "date": self.date}


#LISTEPRODUITS--------------------------------------------------------------
class listeproduit(models.Model):

    commande = models.ForeignKey("commandes", on_delete=models.CASCADE, default=None)
    quantite = models.CharField(max_length=100)
    produit = models.ForeignKey("produits", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.commande

    def dico(self):
        return {"commandes": self.commande, "quantite": self.quantite, "produits": self.produit}
