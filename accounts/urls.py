from django.urls import path, include
from accounts.views import RestaurantOwnerDetail, RestaurantOwnerCreation, RestaurantOwnerList, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('restaurantowner/', RestaurantOwnerList.as_view()),
    path('register/', RestaurantOwnerCreation.as_view()),
    path('restaurantowner/<int:pk>/', RestaurantOwnerDetail.as_view()),
    path('user/', UserCreate.as_view()),
    path('password-reset/', include('django_rest_passwordreset.urls'),
         name="password_reset"),
    # password-reset/confirm/ <= confirmer la modification de mpd
    #JWT urls
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]
