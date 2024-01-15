# accounts/urls.py
from django.urls import path
from .views import signup, user_login, place_details, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('home/', place_details, name='place_details'),
    path('logout/', user_logout, name='logout'),
]
