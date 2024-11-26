"""Definiuje wzroce url dla learning_logs"""

from django.urls import path
from . import views

app_name = 'leraning_logs'
urlpatterns = [
    #strona głowna
    path('', views.index,name='index')

]