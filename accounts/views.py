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
import pyotp

#For auth counting 
import json
from datetime import datetime, timedelta
from django.utils import timezone

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
* To note : * 
request.session[ username, password, count, dateLimit, canAuth]
username & password => user's informations to log in
count => count the connection attemps
dateLimit => date the user can reconnect after being blocked for 5 mins
can Auth => the user is allow to try to authentificate
"""

"""
 Check user's attempt to connect
 @param : request
"""
def checkAuth(request):
    if ('count' in request.session) == False: # If there is no "count" value yet in request.session
        request.session["count"] = 0
        request.session["canAuth"] = True
        request.session.modified = True

    elif request.session["count"] >= 3 and not 'dateLimit' in request.session : # If the user do 3 attempts of connection
        request.session["canAuth"] = False

        today = datetime.now()
        dateLimit = today + timedelta(minutes=10) # add 10 minutes
        request.session["dateLimit"] = dateLimit.isoformat()
        request.session.modified = True

    elif request.session["count"] >= 3 and 'dateLimit' in request.session : # If attempt blocked, deblock after 10 minutes
        dateLimit = datetime.strptime(request.session['dateLimit'], "%Y-%m-%dT%H:%M:%S.%f")
        now = datetime.now()
        if( now > dateLimit): #Compare date now with date limit, if now superior, then the user can attempts to connect again
            del request.session["count"]
            request.session["canAuth"] = True
            del request.session['dateLimit']
            request.session.modified = True

"""
 Know if the user can connect or not
 @param : request
 @return : object { canAuth : [list] }
"""
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def getCanAuth(request):
    if request.method == 'GET':
        try:
            checkAuth(request)
            return Response({"canAuth": request.session['canAuth']}, 200)
        except Exception as e:
            return Response({"error": str(e)})
    else:
        return Response({"method": "Please, try again later."})


"""
 Double authentication by sending email
 @param : request
 @return : object { promo_code : [list] }
"""
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth(request):
        try:
            checkAuth(request)
            # Get user's log in information
            userName = request.data.get('username')
            password = request.data.get('password')

            request.session["username"] = userName
            request.session["password"] = password

            queryset = User.objects.filter(username=userName).all()
            # result = serializers.serialize("json", queryset)
            bool = authenticate(request, username=userName, password=password)


            if (bool is not None) : #and request.session["canAuth"]:
                # Retrieve user information
                informationClient = queryset.values()[::1][0]
                email = informationClient.get("email")
                name = informationClient.get("username")

                totp = pyotp.TOTP('base32secret3232', interval=301)
                code = totp.now() # Create a code
                
                
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
            else :
                count = request.session["count"]
                request.session["count"] =  count + 1
                #del request.session['dateLimit']
            return Response({"auth": request.session["count"], "dateLimit": request.session["dateLimit"] if 'dateLimit' in request.session else None }, 401)
        except Exception as e:
            return Response({"error_auth": str(e)})

"""
 Double authentication : Code verification
 @param : resquest
"""
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def verify2FA(request):
    if request.method == 'POST':
        try:
            #checkAuth(request)
            otp = request.data.get('code')
            totp = pyotp.TOTP('base32secret3232', interval=301)
            if totp.verify(otp) : #and request.session["canAuth"]:

               # inform users if OTP is valid
               if (request.data.get("username") is not None) and (request.data.get("username") is not None) :
                   return TokenObtainPairView.as_view()(request._request)
                   #return Response({"auth": "Le code est conforme"}, 201)
            return Response({"auth": "Le code n'est pas conforme", "code_errr": totp.verify(otp)}, 401)
        except Exception as e:
            return Response({"error": str(e)})
    else:
        return Response({"method": "Please, try again later."})

