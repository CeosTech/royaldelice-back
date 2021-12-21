from django.urls import path

from . import views
from .views import API_keysDetailView

app_name = 'restaurant'


urlpatterns = [
    path('commandes/', views.CommandeView.as_view()),  # /paiement/commandes
    # /paiement/commandes
    path('create-commande', views.CommandeCreateView.as_view()),
    path('update-commande', views.UpdateCommande.as_view()),
    path('nouvelle-commande', views.NouvelleCommande.as_view()),
    path('nombres-nouvelle-commande', views.getNombreNouvellesCommandes),
    path('commande-encours', views.CommandeEnCours.as_view()),
    path('historique-commande', views.HistoriqueCommande.as_view()),
    path('commande', views.CommandeView.as_view()),
    path('commande/<int:pk>/', views.CommandeDetailView.as_view()),
    path('paniers/', views.PanierView.as_view()),  # /paiement/paniers
    path('create-client-secret', views.CreateClientSecret.as_view()),
    path('produits/<int:pk>', views.PanierProduitsView.as_view()),
    # /paiement/paniers-items
    # path('paniers-items/', views.Panier_itemView.as_view()),
    path('stripe/transactions',
         views.ListStripeTransactions.as_view()),
    path('api/keys', views.API_keysView.as_view()),
    path('api/keys/<int:pk>/', API_keysDetailView.as_view()),
]
