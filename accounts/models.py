from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Restaurant, Company
from django.contrib.auth.models import User

import traceback

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


class RestaurantOwner(models.Model):
    nom = models.CharField(max_length=45, null=True)
    prénom = models.CharField(max_length=45, null=True)
    email = models.EmailField(unique=True, default="")
    REQUIRED_FIELDS = ['phone_number', 'company_position', 'email']
    USERNAME_FIELD = 'email'
    phone_number = models.CharField(max_length=45, null=True)
    company_position = models.CharField(max_length=45, null=True)
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        null=True
    )
    company = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        null=True
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    user = RestaurantOwner.objects.filter(
        email=reset_password_token.user.email).get()
    nom = user.nom
    prénom = user.prénom

    email_plaintext_message = """Bonjour {} {},

Vous avez récemment demandé la réinitialisation du mot de passe de votre compte Markus. 
Veuillez suivre la procédure communiquée ci-dessous.

Copiez ce code de modification : {}

Ensuite, revenez sur la page de modification du mot de passe de l’application et renseignez le code reçu par mail dans le champs correspondant.

Enfin, choisissez votre nouveau mot de passe et confirmez-le.

Si vous n’avez pas demandé une réinitialisation de votre mot de passe, ignorez ce email.

Markus vous remercie de votre confiance.

    """.format(nom, prénom, reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Markus"),
        # message:
        email_plaintext_message,
        # from:
        "contact@markus-app.com",
        # to:
        [reset_password_token.user.email]
    )
