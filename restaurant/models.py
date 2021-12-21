from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone


# Create your models here.


class Admin_account(models.Model):  # Ajouter à l'admin Django
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


class Info_Restaurant(models.Model):
    disponibilite_restaurant = models.BooleanField(default=False, null=True)
    disponibilite_livraison = models.BooleanField(default=False, null=True)


class Categorie(models.Model):  # Entrée/Plats/Dessert/
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    # Champs communs pour tous les produits du restaurant
    nom = models.CharField(max_length=100, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey(
        Categorie, null=True, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(null=True, upload_to='static/images')
    prix = models.FloatField(default=0, blank=True)
    disponibilite = models.BooleanField(default=False, null=True)
    commentaire_produit = models.TextField(null=True, blank=True)

    # accompagnement => frite / texmet (categorie)

    # Champs menus spécifiques
    est_menu_sandwichs = models.BooleanField(default=False, null=True)
    est_menu_sandwichs_au_four = models.BooleanField(default=False, null=True)
    est_menu_burgers = models.BooleanField(default=False, null=True)
    est_menu_tacos = models.BooleanField(default=False, null=True)
    est_menu_paninis = models.BooleanField(default=False, null=True)
    est_menu_croque = models.BooleanField(default=False, null=True)
    est_menu_crepe_salee = models.BooleanField(default=False, null=True)
    est_menu_enfant = models.BooleanField(default=False, null=True)
    est_menu_family = models.BooleanField(default=False, null=True)
    est_burger = models.BooleanField(default=False, null=True)
    est_assiette = models.BooleanField(default=False, null=True)
    est_salade_pate = models.BooleanField(default=False, null=True)
    est_crepe_salee = models.BooleanField(default=False, null=True)
    est_panini = models.BooleanField(default=False, null=True)
    est_croque = models.BooleanField(default=False, null=True)
    est_accompagnement = models.BooleanField(default=False, null=True)

    est_pizza_sauce_tomate = models.BooleanField(default=False, null=True)
    est_pizza_creme_fraiche = models.BooleanField(default=False, null=True)
    est_pizza_sauce_barbecue = models.BooleanField(default=False, null=True)

    est_crepe_sucree = models.BooleanField(default=False, null=True)
    est_milkshake = models.BooleanField(default=False, null=True)
    est_smoothie = models.BooleanField(default=False, null=True)
    est_boissons = models.BooleanField(default=False, null=True)
    est_dessert = models.BooleanField(default=False, null=True)

    # Champs spécifiques aux pizzas
    # est_pizzas_sauce_tomate = models.BooleanField(default=False, null=True)
    # est_pizzas_creme_fraiche = models.BooleanField(default=False, null=True)
    # est_pizzas_sauce_barbecue = models.BooleanField(default=False, null=True)
    # categorie pour chacun
    taille = (
        ('Moyenne', 'moyenne'),
        ('Petite', 'petite'),
    )
    taille_pizza = models.CharField(
        choices=taille, max_length=100, blank=True, null=True, default="")

    def __str__(self):
        return self.nom


class Ingredient(models.Model):  # sandwich /
    # Champs commun pour tous les suppléments du restaurant
    nom = models.CharField(max_length=100, unique=True)
    ingredients = (
        ('Pain', 'pain'),
        ('Viande', 'viande'),  # chicken red
        ('Sauce', 'sauce'),  # à séparer
        ('Crudite', 'crudite'),  # sans crudite à ajouter
    )
    type_ingredient = models.CharField(
        choices=ingredients, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nom


# Sauce

class Supplement(models.Model):  # sauce / chedar frites /
    # Champs commun pour tous les suppléments du restaurant
    nom = models.CharField(max_length=100, unique=True)
    supplements = (
        ('Pain', 'pain'),
        ('Viande', 'viande'),
        ('Sur_frite', 'sur_frite'),  # chicken red
        ('Sauce', 'sauce'),  # à séparer
        ('Crudite', 'crudite'),  # sans crudite à ajouter
        ('Fromage', 'fromage'),
        ('Dessert', 'dessert'),
        ('Boisson', 'boisson'),
        ('TaillePizza', 'TaillePizza'),

        # à rajouter pour
    )
    type_supplement = models.CharField(
        choices=supplements, max_length=100, blank=True, null=True)
    prix = models.FloatField(default=0, blank=True)
    disponibilite = models.BooleanField(default=False, null=True)

    # Champs spécifiques
    sup_burgers_sandwichs_assiettes = models.BooleanField(
        default=False, null=True)
    sup_tacos = models.BooleanField(default=False, null=True)
    sup_pizzas = models.BooleanField(default=False, null=True)
    sup_family = models.BooleanField(default=False, null=True)
    sup_salade = models.BooleanField(default=False, null=True)
    sup_sur_frite = models.BooleanField(default=False, null=True)

    sup_milshake_crepe = models.BooleanField(default=False, null=True)
    sup_smoothie = models.BooleanField(default=False, null=True)

    sup_salee = models.BooleanField(default=False, null=True)
    sup_sucree = models.BooleanField(default=False, null=True)

    sup_mix_viande = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.nom

class FormulaireContact(models.Model):
    nom = models.CharField(max_length=26)
    prenom = models.CharField(max_length=26)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    situation = models.CharField(max_length=26)
    echeance = models.CharField(max_length=26)
    ville = models.CharField(max_length=26)
    apport = models.CharField(max_length=26)
    message = models.TextField()
    date_message = models.DateTimeField(default=timezone.now, blank=True)
