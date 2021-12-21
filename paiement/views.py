import json
import string
from random import choices
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, serializers, status, permissions
from .models import *
from restaurant.models import Produit
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from functools import reduce
from django.conf import settings
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import broadcast


# Create your views here.

# mettre en variable d'environnement
# stripe.api_key = "sk_test_51IIvIiJnUZH8vWLUYv5UyL8c1xsuic2ukC0MrsaidKHLcroUAcLv9CE8Ufihgy1oHsNkag9GGQBYGkcNk7RI24Kr006AGZODjU"

# clé de tests 
stripe.api_key = settings.STRIPE_TSK

# clé finale
#stripe.api_key = settings.STRIPE_SECRET_KEY



class API_keysView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = API_keys.objects.all()
    serializer_class = API_keysSerializer


class API_keysDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = API_keys.objects.all()
    serializer_class = API_keysSerializer


class CreateClientSecret(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)

    def filter_queryset(self, queryset):
        queryset = super(CreateClientSecret, self).filter_queryset(queryset)
        return queryset.order_by('-id')

    def post(self, request):
        try:
            paymentIntent = stripe.PaymentIntent.create(
                amount=request.data.get('amount', 0),
                currency='eur', receipt_email=request.data.get('email')
            )
            return Response({"clientSecret": paymentIntent['client_secret']})
        except Exception as e:
            return Response({"error": str(e)})


class ListStripeTransactions(APIView):
    permission_classes = [permissions.AllowAny,]
    def post(self, request, *args, **kwargs):
        try:
            #print(request.data.get('date'))
            transactions = stripe.BalanceTransaction.list(
                created=request.data.get('date'))

            def calcul_prix_avec_frais(item):
                #print(item)
                #frais_stripe = item.fee
                # prix_en_usd = (item.amount - frais_stripe ) / 100
                #print(item.amount)
                #prix_test = (item.amount) / 100.0
                # prix_en_usd = (item.amount) / 100
                # print(item)
                prix_en_euros = (item.amount) / 100
                # prix_euros = round(prix_en_usd / item.exchange_rate, 2)
                return prix_en_euros

            amount = reduce(lambda acc, item : acc + calcul_prix_avec_frais(item),transactions.data, 0)
            nb_commandes = len(transactions['data'])
            return Response({"amount": amount,
                             "nb_commandes": nb_commandes,
                             #  "transactions": transactions
                             })
        except Exception as e:
            return Response({"error": str(e)})


class CommandeView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    def filter_queryset(self, queryset):
        queryset = super(CommandeView, self).filter_queryset(queryset)
        return queryset.order_by('-id')


# Ajouté
class CommandeDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


# class CommandeCreateView(generics.ListCreateAPIView):
#     queryset = Commande.objects.all()
#     serializer_class = CommandeSerializer


class PanierView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer


class NouvelleCommande(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Commande.objects.filter(est_vue=False, est_livre=False)
    serializer_class = CommandeSerializer

    def filter_queryset(self, queryset):
        queryset = super(NouvelleCommande, self).filter_queryset(queryset)
        return queryset.order_by('-id')


def getNombreNouvellesCommandes(request):
    return JsonResponse({"length": Commande.objects.filter(est_vue=False, est_livre=False).count()})


class CommandeEnCours(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Commande.objects.filter(est_vue=True, est_livre=False)
    serializer_class = CommandeSerializer

    def filter_queryset(self, queryset):
        queryset = super(CommandeEnCours, self).filter_queryset(queryset)
        return queryset.order_by('-id')


class HistoriqueCommande(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Commande.objects.filter(
        est_vue=True, est_livre=True).order_by('-date_commande')
    serializer_class = CommandeSerializer

    def filter_queryset(self, queryset):
        queryset = super(HistoriqueCommande, self).filter_queryset(queryset)
        return queryset.order_by('-id')


class CommandeCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CommandeSerializer
    produit_serializer_class = Panier_nonnullproduitSerializer
    queryset = Commande.objects.all()


    def post(self, request, format=None):
        panier = Panier()
        panier.save()  # il faut un id pour les relation many to many

        infos_menus = request.data.get('panier').get('infos_menus')
        panier.infos_menus = infos_menus
        panier.save()

       # produits = request.data.get('panier').get('produits')
       # panier.produits = produits
       # panier.save()

        produits = request.data.get('panier').get('produits')

        # if produits != None:
        #     if len(produits) > 0:
        #         accompagnement = produits[0].get('accompagnement')
        #         panier.produits.accompagnement = accompagnement
        #         panier.save()

        detailedproduits = []

        for produit_dict in produits:
            produit_id = produit_dict.get('produit_id')
            print(produit_id)
            produit = Produit.objects.get(id=produit_id)
            panier_produit = Panier_produit(
                produit=produit, **produit_dict)
            panier_produit.save()
            panier.produits.add(panier_produit)
            detailedproduits.append(self.produit_serializer_class(panier_produit).data)

        # print(panier.menus.all())

        client = Client.objects.create(**request.data.get('client'))

        while True:
            code = ''.join(
                choices(string.ascii_uppercase + '0123456789', k=5))
            if Commande.objects.filter(reference=code).count() == 0:
                break

        commande = Commande.objects.create(
            panier=panier,
            client=client,
            commentaire=request.data.get('commentaire'),
            # livraison=request.data.get('livraison'),
            methode_vente=request.data.get('methode_vente'),
            prix_totale=request.data.get('prix_totale'),
            reference=code
        )
        data = {}
        commandejson = {}
        commandejson['commande'] = self.serializer_class(commande).data
        commandejson['produits'] = detailedproduits
        data['message'] = commandejson
        return Response(self.serializer_class(commande).data, status=status.HTTP_201_CREATED)


# class Panier_itemView(generics.ListAPIView):
#     queryset = Panier_item.objects.all()
#     serializer_class = Panier_itemSerializer


class UpdateCommande(APIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = CommandeSerializer
    produit_serializer_class = Panier_nonnullproduitSerializer

    def put(self, request):
        commande_id = request.data.get('id')
        commande = get_object_or_404(Commande, id=commande_id)
        produits = commande.panier.produits
        detailedproduits = []

        for panier_produit in produits.all():
            produit_id = panier_produit.produit.id
            print(produit_id)
            produit = Produit.objects.get(id=produit_id)
            detailedproduits.append(self.produit_serializer_class(panier_produit).data)

        commande.est_vue = request.data.get('est_vue', commande.est_vue)
        commande.est_livre = request.data.get('est_livre', commande.est_livre)
        commande.save(update_fields=['est_livre', 'est_vue'])

        data = {}
        commandejson = {}
        commandejson['commande'] = self.serializer_class(commande).data
        commandejson['produits'] = detailedproduits
        data['message'] = commandejson
        livre = request.data.get('livre')
        if not livre:
            broadcast.sendOrder(commandejson)

        return Response(status=status.HTTP_204_NO_CONTENT)

class PanierProduitsView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Panier_produit.objects.all()
    serializer_class = Panier_produitSerializer
