"""Definiuje wzorce adresów URL dla apliakcji users"""

from django.urls import path,include
from . import views

app_name = 'users'
urlpatterns = [
#Dołączanie domyślnych adresów URL uwierzytelniania
path('logout/',views.user_logout,name='user_logout'),
path('', include('django.contrib.auth.urls')),
#Strona rejestracji
path('register/',views.register,name='register'),

]