from rest_framework import serializers
from .models import *

from restaurant.serializers import ProduitSerializer, NonNullProduitSerializer

class API_keysSerializer(serializers.ModelSerializer):
    class Meta:
       model = API_keys
       fields = "__all__"


class PanierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Panier
        fields = "__all__"

class Panier_produitSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer()

    class Meta:
        model = Panier_produit
        fields = "__all__"
        
class Panier_nonnullproduitSerializer(serializers.ModelSerializer):
    produit = NonNullProduitSerializer()

    class Meta:
        model = Panier_produit
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CommandeSerializer(serializers.ModelSerializer):
    panier = PanierSerializer()
    client = ClientSerializer()

    class Meta:
        model = Commande
        fields = "__all__"

    def create(self, validated_data):
         panier_data = validated_data.pop('panier')
         panier = Panier.objects.create(**panier_data)
         client_data = validated_data.pop('client')
         client = Client.objects.create(**client_data)
         commande = Commande.objects.create(
             **validated_data, panier=panier, client=client)
         return commande
