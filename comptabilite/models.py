from django.db import models
from django.conf import settings

# Create your models here.


class Facture(models.Model):
    TVA1 = 5.5
    TVA2 = 10
    TVA3 = 20

    TVA = (
        (TVA1, '5.5'),
        (TVA2, '10'),
        (TVA3, '20')
    )
    montantHT = models.FloatField(blank=True)
    montantTVA = models.FloatField(choices=TVA, blank=True)
    fournisseur = models.CharField(max_length=15, blank=True)
    date_achat = models.BigIntegerField(blank=True, null=True)
    photo_facture = models.ImageField(
        upload_to='static/images', blank=True, null=True)
