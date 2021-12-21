from django.shortcuts import render

from main.serializers import *
from main.models import *
from rest_framework import generics,permissions


class CompanyList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RestaurantList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


