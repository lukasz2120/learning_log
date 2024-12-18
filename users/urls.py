"""Definiuje wzorce adresów URL dla apliakcji users"""

from django.urls import path,include
from . import views

app_name = 'users'
urlpatterns = [
#Dołączanie domyślnych adresówu URL uwierzytelniania
path('', include('django.contrib.auth.urls')),
#Strona rejestracji
path('register/',views.register,name='register'),
]