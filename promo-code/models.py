from django.db import models
from django.db.models.enums import Choices
from restaurant.models import Produit, Supplement
# Create your models here.
from functools import reduce


class API_keys(models.Model):
    stripe_public_key = models.TextField(null=True, blank=True)
    google_maps_key = models.TextField(null=True, blank=True)