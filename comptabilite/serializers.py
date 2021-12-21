from rest_framework import serializers
from comptabilite.models import *
from .models import *


class FactureSerializer(serializers.ModelSerializer):
    #date_achat = serializers.DateField(format="%d/%m/%Y", input_formats="%d/%m/%Y")

    class Meta:
        model = Facture
        fields = ["id",
                  'montantHT',
                  "montantTVA",
                  "fournisseur",
                  "date_achat",
                  "photo_facture"
                  ]
