from django.shortcuts import render
from .models import Topic

def index(request):
    """Strona głowna dla aplikacji Learning log."""
    return render(request, 'D:\\projects\\learning_log\\learning_logs\\templates\\learning_logs\\index.html')

def topics(request):
    """Wyświetlanie wszystkich tematów"""
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return render(request, 'D:\\projects\\learning_log\\learning_logs\\templates\\learning_logs\\topics.html', context)

def topic(request,topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request,'D:\\projects\\learning_log\\learning_logs\\templates\\learning_logs\\topics.html',context)