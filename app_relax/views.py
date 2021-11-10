from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app_relax/index.html')

def settings(request):
    return render(request, 'app_relax/settings.html')

def panic_button(request):
    return render(request, 'app_relax/panic-button.html')

def user(request):
    return render(request, 'app_relax/user.html')

def tips(request):
    return render(request, 'app_relax/tips.html')

def stats(request):
    return render(request, 'app_relax/stats.html')