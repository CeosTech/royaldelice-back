from django.db import models
from django.db.models.enums import Choices
from restaurant.models import Produit, Supplement
# Create your models here.
from functools import reduce


class API_keys(models.Model):
    stripe_public_key = models.TextField(null=True, blank=True)
    google_maps_key = models.TextField(null=True, blank=True)


class Panier_produit(models.Model):
    # supplement = models.TextField(null=True, blank=True)
    quantite = models.IntegerField()
    supplements = models.TextField(null=True)
    information = models.TextField(null=True)
    produit = models.ForeignKey(
        Produit, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return str(self.produit.nom)

    def totale(self):
        return round(self.produit.prix * self.quantite, 2)


class Panier(models.Model):  # Posibilité de l'ajouter aux champs des tables Produit et Menu
    # id = models.AutoField(primary_key=True)
    # panier_items = models.ManyToManyField(Panier_item)
    produits = models.ManyToManyField(Panier_produit, blank=True)
    infos_menus = models.TextField(null=True)

    def __str__(self):
        return str(self.produit.id)

    def totale(self):
        return round(reduce(lambda acc, item: acc + item.totale(), self.produits.all(), 0) + reduce(
            lambda acc, item: acc + item.totale(), self.menus.all(), 0), 2)


# class Panier(models.Model):
#   infos_produits = models.TextField(null=True)
#   infos_menus = models.TextField(null=True)
#  infos_panier = models.TextField(null=True)

# def __str__(self):
#     return str(self.id)

# def totale(self): return round(reduce(lambda acc, item: acc + item.totale(), self.produits.all(), 0) + reduce(
# lambda acc, item: acc + item.totale(), self.menus.all(), 0), 2)


class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=250)
    ville = models.CharField(max_length=32)
    code_postale = models.CharField(max_length=32, null=False)
    montant = models.FloatField(default=0.0, null=False)

    def __str__(self):
        return self.nom + ' ' + self.prenom


class Commande(models.Model):
    date_commande = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(null=True, blank=True)
    methode_vente = models.CharField(max_length=50, null=True)  # Livraison ou À emporter
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, null=True)
    prix_totale = models.FloatField(default=0.0)

    est_vue = models.BooleanField(default=False)
    est_livre = models.BooleanField(default=False)

    reference = models.CharField(default='', max_length=5, null=True)

    def __str__(self):
        return str(self.id)

    def totale(self):
        return self.panier.totale()