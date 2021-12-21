from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import generics
from accounts.serializers import RestaurantOwnerSerializer, UserSerializer
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import generics, permissions
from .models import RestaurantOwner
from django_filters.rest_framework import DjangoFilterBackend

permission = permissions.AllowAny


class RestaurantOwnerCreation(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer


class RestaurantOwnerList(generics.ListCreateAPIView):
    permission_classes = [permission]
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']


class RestaurantOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permission]
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer


class UserCreate(generics.CreateAPIView):
    permission_classes = [permission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
