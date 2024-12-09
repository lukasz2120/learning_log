"""Definiuje wzroce url dla learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #strona głowna
    path('', views.index,name='index'),
    #Wyświetlanie wszystkich tematów
    path('topics/', views.topics,name='topics'),
    #Strona szczegółowa dotycząca poszczególnego tematu
    path('topics/(<int:topic_id>)/',views.topic,name='topic')

]