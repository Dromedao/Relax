from ast import NodeTransformer
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, NoteForm

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