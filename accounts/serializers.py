from rest_framework import serializers
from accounts.models import *
from main.models import *
from main.serializers import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {"required": False,
                                     "allow_null": True, 'write_only': True}}
        extra_kwargs = {"username": {"required": False, "allow_null": True}}
        #extra_kwargs = {"forgotKey": {"required": False, "allow_null": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User(**validated_data)
        user.set_password(password)
        user.username = email
        user.email = email
        user.save()
        return user

    def get_validation_exclusions(self):
        exclusions = super(UserSerializer, self).get_validation_exclusions()
        return exclusions + ['username', 'password']


class RestaurantOwnerSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(many=False)
    user = UserSerializer(many=False, required=False)
    company = CompanySerializer(many=False)

    class Meta:
        model = RestaurantOwner
        fields = [
            "id",
            "nom",
            "prénom",
            "email",
            "phone_number",
            "company_position",
            "restaurant",
            "company",
            "user"
        ]
        depth = 2

    def create(self, data, **kwargs):

        company_data = data['company']
        company = Company.objects.create(
            name=company_data["name"],
            address=company_data["address"],
            postal_code=company_data["postal_code"],
            city=company_data["city"],
            capital=company_data["capital"],
            SIRET_number=company_data["SIRET_number"],
            retirement_fund_name=company_data["retirement_fund_name"],
            retirement_fund_address=company_data["retirement_fund_address"],
            retirement_fund_city=company_data["retirement_fund_city"],
            retirement_fund_postal_code=company_data["retirement_fund_postal_code"]
        )
        company.save()

        restaurant_data = data['restaurant']
        restaurant = Restaurant.objects.create(
            name=restaurant_data["name"],
            address=restaurant_data["address"],
            postal_code=restaurant_data["postal_code"],
            city=restaurant_data["city"],
            phone_number=restaurant_data["phone_number"]
        )
        restaurant.save()

        user_data = data['user']
        user = User.objects.create(
            username=user_data["username"],
            email=user_data["username"]
        )
        user.set_password(user_data["password"])
        user.save()

        owner = RestaurantOwner.objects.create(
            nom=data["nom"],
            prénom=data["prénom"],
            email=data["email"],
            phone_number=data["phone_number"],
            company_position=data["company_position"],
            restaurant=restaurant,
            company=company,
            user=user
        )
        owner.save()
        return owner

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        password = user_data.pop('password')
        user.set_password(password)
        user.save()
        company_data = validated_data.pop('company')
        company = instance.company
        instance.company.name = company_data.get('name', instance.company.name)
        company.address = company_data.get('address', company.address)
        company.postal_code = company_data.get(
            'postal_code', company.postal_code)
        company.city = company_data.get('city', company.city)
        company.capital = company_data.get('capital', company.capital)
        company.SIRET_number = company_data.get(
            'SIRET_number', company.SIRET_number)
        company.retirement_fund_name = company_data.get(
            'retirement_fund_name', company.retirement_fund_name)
        company.retirement_fund_address = company_data.get(
            'retirement_fund_address', company.retirement_fund_address)
        company.retirement_fund_city = company_data.get(
            'retirement_fund_city', company.retirement_fund_city)
        company.retirement_fund_postal_code = company_data.get(
            'retirement_fund_postal_code', company.retirement_fund_postal_code)
        company.save()
        restaurant_data = validated_data.pop('restaurant')
        restaurant = instance.restaurant
        restaurant.name = restaurant_data.get('name', restaurant.name)
        restaurant.address = restaurant_data.get('address', restaurant.address)
        restaurant.postal_code = restaurant_data.get(
            'postal_code', restaurant.postal_code)
        restaurant.city = restaurant_data.get('city', restaurant.city)
        restaurant.phone_number = restaurant_data.get(
            'phone_number', restaurant.phone_number)
        restaurant.save()
        instance.nom = validated_data.get('nom', instance.nom)
        instance.prénom = validated_data.get('prénom', instance.prénom)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.company_position = validated_data.get(
            'company_position', instance.company_position)
        instance.save()

        return instance
