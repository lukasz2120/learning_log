from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def register(request):
    """Rejestracja nowego użytkownika"""
    if request.method != "POST":
        #wyświetlanie pustego formularza
        form = UserCreationForm()
    else:
        #Przetwarzanie wypełnionego formularza
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #Zalogowanie użytkownika, a następnie przekierowanie na 
            #główna strone
            login(request,new_user)
            return redirect('learning_logs:index')
        
    #Wyświetlenie pustego formularza
    context = {'form': form}
    return render(request, 'registration/register.html',context)

@api_view(['POST', 'GET'])
@login_required
def user_logout(request):
    logout(request)
    return render(request,'registration/logged_out.html', {})
