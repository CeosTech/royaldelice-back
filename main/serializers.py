from rest_framework import serializers
from main.models import *
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id",
                  "name",
                  "address",
                  "postal_code",
                  "city",
                  "capital",
                  "SIRET_number",
                  "retirement_fund_name",
                  "retirement_fund_address",
                  "retirement_fund_city",
                  "retirement_fund_postal_code"]


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id",
                  "name",
                  "address",
                  "postal_code",
                  "city",
                  "phone_number"]





