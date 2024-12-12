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
    path('topics/(<int:topic_id>)/',views.topic,name='topic'),
    #Dodawanie nowego tematu
    path('new_topic/',views.new_topic,name='new_topic'),
    #Dodawanie nowego wpisu
    path('new_entry/(<int:topic_id>)/',views.new_entry,name='new_entry'),
    #Strona przeznaczona do edycji wpisu
    path('edit_entry/<int:entry_id>/', views.edit_entry,name="edit_entry")
    

]