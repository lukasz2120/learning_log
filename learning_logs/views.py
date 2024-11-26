from django.shortcuts import render

def index(request):
    """Strona głowna dla aplikacji Learning log."""
    return render(request, 'D:\\projects\\learning_log\\learning_logs\\templates\\learning_logs\\index.html')