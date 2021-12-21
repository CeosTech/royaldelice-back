from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from comptabilite.serializers import *
from comptabilite.models import *
from rest_framework import generics,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class FactureList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ['date_achat']

    def filter_queryset(self, queryset):
        queryset = super(FactureList, self).filter_queryset(queryset)
        return queryset.order_by('-id')


class FactureDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
