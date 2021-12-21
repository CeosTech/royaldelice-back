from django.urls import path
from comptabilite.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # List views
    path('facture/',FactureList.as_view()),

    # Detail views
    path('facture/<int:pk>/',FactureDetail.as_view()),
     ]
urlpatterns = format_suffix_patterns(urlpatterns)