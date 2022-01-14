""" 
Library for EMAIL + 2FA
"""
from rest_framework_simplejwt.views import TokenObtainPairView
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import time
import pyotp

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

"""
 Double authentication by sending email
 @param : resquest
 @return : object { promo_code : [list] }
"""
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth(request):
    if request.method == 'POST':
        try:
            userName = request.data.get('username')
            password = request.data.get('password')

            request.session["username"] = userName
            request.session["password"] = password

            queryset = User.objects.filter(username=userName).all()
            # result = serializers.serialize("json", queryset)
            bool = authenticate(request, username=userName, password=password)

            if bool is not None:
                # Retrieve user information
                informationClient = queryset.values()[::1][0]
                email = informationClient.get("email")
                name = informationClient.get("username")

                totp = pyotp.TOTP('base32secret3232', interval=300)
                code = totp.now() # Create a code
                print(code)
                
                
                # ===============SEND MAIL ================
                html = """\
<html>
  <head>
  </head>
  <body style="margin: auto">
  <div style="width: 70vw; margin: auto;">
  <div style="background-color: #04295d; border-top-left-radius: 80px 80px; border-top-right-radius: 80px 80px;">
  <center><img src="https://res.cloudinary.com/hv5opcs4e/image/upload/v1642005619/img/Logo_complet_application_markus_-_blanc_tcu5ub.png" alt="banniere_Markus"  style="height: 20vh;"/></center>
  </div>
  <div style="margin-left: 10%; padding-top: 5%; font-size:1.5em;">
        <p>Bonjour {name} !<br>
        Pour vous connecter au compte Markus, veuillez entrer le code suivant :<br>
        </p>
    </div>
        <span style="background-color: #04295d; font-size: 2em; padding: 0.2vw 3vw 0.2vw 3vw; color: white; margin-left: 10%;"><b>{code}</b></span>
    <div style="margin-left: 10%; padding-top: 1%; padding-bottom: 5%; font-size:1.5em;">
        <p> A bientôt ! <br/> La team MARKUS</p>
    </div>
    <img src="https://res.cloudinary.com/hv5opcs4e/image/upload/v1642005619/img/Banni%C3%A8re_Markus_fkaqxi.png" alt="banniere_Markus"  style="height: auto; width: 100%; border-bottom-left-radius: 80px 80px; border-bottom-right-radius: 80px 80px;"/>
  </div>
  </body>
</html>
""".format(name = name, code = code)
                #The mail addresses and password
                sender_address = "ceostech.dev@gmail.com"
                sender_pass = "CeosTech93_"
                receiver_address = email
                #Setup the MIME
                message = MIMEMultipart()
                message["From"] = sender_address
                message["To"] = receiver_address
                message["Subject"] = "Votre code d'identification"   #The subject line
                #The body and the attachments for the mail
                message.attach(MIMEText(html, 'html'))
                #Create SMTP session for sending the mail
                session = smtplib.SMTP("smtp.gmail.com", 587) #use gmail with port
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
                # ===============================
                
                # Send a code if the password/email combinaition is correct
                return Response(200)

            # Error if the password/email combinaition is incorrect.
            return Response({"auth": "error"}, 401)
        except Exception as e:
            return Response({"error": str(e)})
    else:
        return Response({"method": "Please, try again later."})

"""
 Double authentication : Code verification
 @param : resquest
"""
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def verify2FA(request):
    if request.method == 'POST':
        try:
            otp = request.data.get('code')
            print("=====otp====")
            print(otp)
            totp = pyotp.TOTP('base32secret3232', interval=300)
            if totp.verify(otp):
               # inform users if OTP is valid
               if (request.data.get("username") is not None) and (request.data.get("username") is not None) :
                   return TokenObtainPairView.as_view()(request._request)
                   #return Response({"auth": "Le code est conforme"}, 201)
            return Response({"auth": "Le code n'est pas conforme"}, 401)
        except Exception as e:
            return Response({"error": str(e)})
    else:
        return Response({"method": "Please, try again later."})

