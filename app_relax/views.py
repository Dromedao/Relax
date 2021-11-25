from ast import NodeTransformer
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, NoteForm, SentimientoForm
import requests

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

def notes(request):
    notas = Nota.objects.all()
    context = {'notes': notas}
    return render(request, 'app_relax/notes.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect("http://localhost:8000/home/")
    else:
        form = UserRegisterForm()
    context = {'form' : form }
    return render(request, 'app_relax/register.html', context)  

# def entrevista(request):
#     return render(request, )

def nota(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.user = current_user
            nota.save()
            messages.success(request, 'Nota subida')
            return redirect("http://localhost:8000/notes/")
    else:
        form = NoteForm()
    return render(request, 'app_relax/newnote.html', {'form' : form })

# def perros(request):
#     response = request.GET.get('https://dog.ceo/api/breeds/image/random').json()
#     return render(request, 'app_relax/perros.html', {'response': response})

from .services import get_dog

def hello_user(requests):
    context = {
        'message': get_dog()
    }
    return render(requests, 'app_relax/perros.html', context)

def FormularioView(request):
    if request.method == "POST":
        current_user = get_object_or_404(User, pk=request.user.pk)
        form = SentimientoForm(request.POST)
        if form.is_valid():
            forma = form.save(commit=False)
            forma.user = current_user
            forma.save()
    else:
        form = SentimientoForm()
    return render(request, "app_relax/formulario.html", {'form' : form })

# def hello_user(requests):
#     params = { 'order': 'desc' }

#     context = {
#         'message': get_username(params)
#     }
#     return render(requests, 'app_relax/perros.html', context)