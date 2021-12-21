from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status, permissions
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

categories_produits = ['burgers', 'boissons',
                       'desserts', 'sides', 'poutines', 'entrees']


class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Admin_accountView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Admin_account.objects.all()
    serializer_class = Admin_accountSerializer

class Admin_accountDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Admin_account.objects.all()
    serializer_class = Admin_accountSerializer



class Info_RestaurantView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Info_Restaurant.objects.all()
    serializer_class = Info_RestaurantSerializer

class Info_RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Info_Restaurant.objects.all()
    serializer_class = Info_RestaurantSerializer



class CategorieView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer




class ProduitView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['categorie']

    def filter_queryset(self, queryset):
        queryset = super(ProduitView, self).filter_queryset(queryset)
        return queryset.order_by('nom')


class ProduitDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer



class IngredientView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = "__all__"

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class SupplementView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = "__all__"

    def filter_queryset(self, queryset):
        queryset = super(SupplementView, self).filter_queryset(queryset)
        return queryset.order_by('prix')

class SupplementDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer


class UpdateProduitDisponibilte(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = ProduitSerializer

    def put(self, request):
        produit_id = request.data.get('id')
        produit = get_object_or_404(Produit, id=produit_id)
        produit.disponibilite = request.data.get(
            'disponibilite', produit.disponibilite)
        produit.save(update_fields=['disponibilite'])
        return Response(status=status.HTTP_204_NO_CONTENT)

class FormulaireContactView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = FormulaireContactSerializer
    queryset = FormulaireContact.objects.all()


class FormulaireContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = FormulaireContactSerializer
    queryset = FormulaireContact.objects.all()
