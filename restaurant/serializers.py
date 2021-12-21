from collections import OrderedDict
from rest_framework import serializers
from restaurant.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        extra_kwargs = {"username": {"required": False, "allow_null": True}}
        # extra_kwargs = {"forgotKey": {"required": False, "allow_null": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        # email = validated_data.pop('email')
        user = User(**validated_data)
        user.set_password(password)
        user.username = email
        user.email = email
        user.save()
        return user

    def get_validation_exclusions(self):
        exclusions = super(UserSerializer, self).get_validation_exclusions()
        return exclusions + ['username']


class Admin_accountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=False)

    class Meta:
        model = Admin_account
        fields = [
            "id",
            "user",
        ]
        depth = 2

    def create(self, data, **kwargs):
        user_data = data['user']
        user = User.objects.create(
            username=user_data["username"],
        )
        user.set_password(user_data["password"])
        user.save()

        admin_account = Admin_account.objects.create(
            user=user
        )
        admin_account.save()
        return admin_account

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        password = user_data.pop('password')
        user.set_password(password)
        user.save()
        return instance


class Info_RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info_Restaurant
        fields = "__all__"


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"

class NonNullProduitSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super(NonNullProduitSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None and result[key]])
    class Meta:
        model = Produit
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = "__all__"

class FormulaireContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaireContact
        fields = ["id",
                  "nom",
                  "prenom",
                  "email",
                  "telephone",
                  "situation",
                  "echeance",
                  "ville",
                  "apport",
                  "message",
                  "date_message",
                  ]

