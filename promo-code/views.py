import json
import string
from random import choices
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, serializers, status, permissions
from django.core.serializers import serialize

from restaurant.serializers import NonNullProduitSerializer
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

import stripe
from functools import reduce
from django.conf import settings
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime


# Create your views here.

# clé de tests
stripe.api_key = settings.STRIPE_SECRET_KEY

# clé finale
#stripe.api_key = settings.STRIPE_SECRET_KEY

"""
* Promotion code 
"""
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def index(self):
     return Response({"promo_code" : "Salut !"})

"""
 Retrieve all the promotional code
 @param : resquest
 @return : object { promo_code : [list] }
"""
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get(request):
        if request.method == 'GET':
            try:
                promotion_code = stripe.PromotionCode.list(limit=1) # We limit the code render by 1
                code = [] # Put all the code in the table
                i = 0
                while i < len(promotion_code.data): # Retrieve the codes and put in the codelist
                    if(promotion_code.data[i].active):
                        code.append(promotion_code.data[i].code)
                    i=i+1
                return Response({"promo_code" : code})# Return reponse in json's object
            except Exception as e:
                return Response({"error": str(e)})
        else :
            return Response({"promo_code" : "Méthode non conforme"})

"""
 Check if the code provided by the client is valid or not
 @param : request, code (from URL)
 @return : object { check : [Boolean], percent }
"""
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def checkCode(request, code):
        if request.method == 'GET':
            try:
                promotion_code = stripe.PromotionCode.list(limit=1)
                code_list = [] # stock the codes
                percent = [] # stock the percent_off
                i = 0
                while i < len(promotion_code.data): # Retrieve the codes and put in the codelist
                    if(promotion_code.data[i].active):
                        code_list.append(promotion_code.data[i].code) # add code value
                        percent.append(promotion_code.data[i].coupon.percent_off) # add percent_off value
                    i=i+1
                res = code in code_list # check if the code exist
                if res :
                    index = code_list.index(code)
                    percent = percent[index]
                else :
                    percent = 0
                return Response({"check" : res, "percent_off" : percent})
            except Exception as e:
                return Response({"error": str(e)})
        else :
            return Response({"promo_code" : "Méthode non conforme"})



