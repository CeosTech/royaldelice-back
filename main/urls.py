from django.urls import path
from main.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # List views
    path('company/',CompanyList.as_view()),
    path('restaurant/',RestaurantList.as_view()),

    # Detail views
    path('company/<int:pk>/',CompanyDetail.as_view()),
    path('restaurant/<int:pk>/',RestaurantDetail.as_view()),


]
urlpatterns = format_suffix_patterns(urlpatterns)
