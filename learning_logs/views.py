from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
from rest_framework.decorators import api_view

from .models import Topic,Entry
from .forms import TopicForm,EntryForm


def index(request):
    """Strona głowna dla aplikacji Learning log."""
    return render(request, 'learning_logs/index.html')

@api_view(['GET'])
@login_required
def topics(request):
    """Wyświetlanie wszystkich tematów"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@api_view(['GET'])
@login_required
def topic(request,topic_id):
    """Wyświetla pojedyńczy temat i wszystkie powiązane z nim wpisy"""
    topic = Topic.objects.get(id=topic_id)
    #Upewniamy się że dany temat należy do użytkownika
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request,'learning_logs/topic.html',context)

@api_view(['POST', 'GET'])
@login_required
def new_topic(request):
    """Dodaj nowy temat"""
    if request.method != "POST":
        #Nieprzekazano żadnych danych, należy utworzyć pusty formularz.
        form = TopicForm()
    else:
        #Przekazano dane i należy je przetworzyć
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topics = form.save(commit=False) 
            new_topics.owner = request.user
            form.save()
            return redirect('learning_logs:topics')
    
    #Wyświetlanie pustego formularza
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)

@api_view(['POST', 'GET'])
@login_required
def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla konkretnego tematu"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nie przekazano danych, należy utworzyć pusty formularz
        form = EntryForm()
    else:
        #Przekazano dane za pomocą żądania POST
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
        
    #Wyświetlanie pustego formularza
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html',context)

@api_view(['POST', 'GET'])
@login_required
def edit_entry(request,entry_id):
    """Edycja insteniejącego wpisu"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Nie przekazano danych, należy utworzyć pusty formularz
        form = EntryForm(instance=entry)
    else:
        #Przekazano dane za pomocą żądania POST
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic.id)
    
    context = {'entry': entry, 'topic': topic,'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
