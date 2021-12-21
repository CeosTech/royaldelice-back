from django.db import models

import traceback


class Company(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=45)
    capital = models.FloatField()
    SIRET_number = models.CharField(max_length=14)
    retirement_fund_name = models.CharField(max_length=45)
    retirement_fund_address = models.CharField(max_length=45)
    retirement_fund_city = models.CharField(max_length=45)
    retirement_fund_postal_code = models.CharField(max_length=5)


class Restaurant(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)





