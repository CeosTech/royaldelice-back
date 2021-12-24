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
    supplement = models.BooleanField(default=False, null=True)
    commentaire_produit = models.TextField(null=True, blank=True)

    # accompagnement => frite / texmet (categorie)

    # Champs menus spécifiques
    # est_menu_sandwichs = models.BooleanField(default=False, null=True)
    # est_menu_sandwichs_au_four = models.BooleanField(default=False, null=True)
    # est_menu_burgers = models.BooleanField(default=False, null=True)
    # est_menu_tacos = models.BooleanField(default=False, null=True)
    # est_menu_paninis = models.BooleanField(default=False, null=True)

    # est_menu_crepe_salee = models.BooleanField(default=False, null=True)
    # est_menu_enfant = models.BooleanField(default=False, null=True)
    # est_menu_family = models.BooleanField(default=False, null=True)
    # est_assiette = models.BooleanField(default=False, null=True)
    # est_salade_pate = models.BooleanField(default=False, null=True)
    # est_crepe_salee = models.BooleanField(default=False, null=True)
    # est_panini = models.BooleanField(default=False, null=True)
    # est_croque = models.BooleanField(default=False, null=True)

    # est_pizza_sauce_tomate = models.BooleanField(default=False, null=True)
    # est_pizza_creme_fraiche = models.BooleanField(default=False, null=True)
    # est_pizza_sauce_barbecue = models.BooleanField(default=False, null=True)

    # est_crepe_sucree = models.BooleanField(default=False, null=True)
    # est_milkshake = models.BooleanField(default=False, null=True)
    # est_smoothie = models.BooleanField(default=False, null=True)
    # est_accompagnement = models.BooleanField(default=False, null=True)
    # est_burger = models.BooleanField(default=False, null=True)
    # est_boissons = models.BooleanField(default=False, null=True)
    # est_dessert = models.BooleanField(default=False, null=True)
    # est_entree = models.BooleanField(default=False, null=True)

    # Champs spécifiques aux pizzas
    # est_pizzas_sauce_tomate = models.BooleanField(default=False, null=True)
    # est_pizzas_creme_fraiche = models.BooleanField(default=False, null=True)
    # est_pizzas_sauce_barbecue = models.BooleanField(default=False, null=True)
    # categorie pour chacun
    # taille = (
    #     ('Moyenne', 'moyenne'),
    #     ('Petite', 'petite'),
    # )
    # taille_pizza = models.CharField(
    #     choices=taille, max_length=100, blank=True, null=True, default="")

    def __str__(self):
        return self.nom


class TypeIngredient(models.Model):  # Choisir le type d'ingrédient
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Ingredient(models.Model):  # sandwich /
    # Champs commun pour tous les suppléments du restaurant
    typeIngredient = models.ForeignKey(
        TypeIngredient, null=True, on_delete=models.CASCADE, blank=True)
    categorie = models.ForeignKey(
        Categorie, null=True, on_delete=models.CASCADE, blank=True)
    disponibilite = models.BooleanField(default=False, null=True)
    nom = models.CharField(max_length=100, unique=True)
    """ ingredients = (
        ('Pain', 'pain'),
        ('Viande', 'viande'),  # chicken red
        ('Sauce', 'sauce'),  # à séparer
        ('Crudite', 'crudite'),  # sans crudite à ajouter
    )
    type_ingredient = models.CharField(
        choices=ingredients, max_length=100, blank=True, null=True) """
    """ type_ingredient = models.CharField(
        choices=[(o.id, str(o)) for o in TypeIngredient.objects.filter(nom=nom)], max_length=100, blank=True, null=True) """

    def __str__(self):
        return self.nom


# Sauce

class TypeSupplement(models.Model):  # Choisir le type d'ingrédient
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom


class Supplement(models.Model):  # sauce / chedar frites /
    # Champs commun pour tous les suppléments du restaurant
    nom = models.CharField(max_length=100, unique=True)
    type_supplement = models.ForeignKey(
        TypeSupplement, null=True, on_delete=models.CASCADE, blank=True)
    categorie = models.ForeignKey(
        Categorie, null=True, on_delete=models.CASCADE, blank=True)
    prix = models.FloatField(default=0, blank=True)
    disponibilite = models.BooleanField(default=False, null=True)
    # Champs spécifiques
    """ choix = tuple(TypeSupplement.objects.all().values_list())
    type = models.CharField(max_length=5, choices=choix, default=1) """

    def __str__(self):
        return self.nom


""" labels = TypeSupplement.objects.values_list('nom', flat=True)
labels = list(labels)

for label in labels:
    Supplement.add_to_class(label, models.BooleanField(default=False, null=True)) """


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


class ZoneLivraison(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    montant = models.FloatField(default=0, blank=True)
    description = models.CharField(max_length=2000)
    frais = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.nom
