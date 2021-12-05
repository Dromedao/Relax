from ast import NodeTransformer
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView
from django.contrib import messages
from .forms import DogsForm, HowDoYouFeelForm, UserRegisterForm, NoteForm, SentimientoForm
import datetime
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

def mp3player(request):
    return render(request, "app_relax/reproductor.html")

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

# def DogsView(request):
#     current_user = get_object_or_404(User, pk=request.user.pk)
#     if request.method == "POST":
#         form = DogsForm(request.POST)
#         if form.is_valid():
#             dog = form.save(commit=False)
#             dog.user = current_user
#             dog.save()
#             messages.success(request, 'Nota subida')


def hello_user(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = DogsForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.user = current_user
            dog.imagen = request.POST.get("imagen")
            dog.save()
            messages.success(request, 'Perro guardado')
    else:
        form = DogsForm()
    imagen_perro = get_dog()
    listado = {
        "form" : form, 
        "message" : imagen_perro
    }
    print(form)
    return render(request, 'app_relax/perros.html', listado)

def MostrarPerros(request):
    perros = Dog.objects.all()
    context = {'dogs': perros}
    return render(request, 'app_relax/owndogs.html', context)

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

def HowDoYouFeelView(request):
    producto = get_object_or_404(Profile, user = request.user)

    data = {
        'form': HowDoYouFeelForm(instance=producto)
    }

    if request.method == "POST":
        #current_user = get_object_or_404(User, pk=request.user.pk)
        form = HowDoYouFeelForm(data=request.POST, instance=producto, files=request.FILES)
        #form = HowDoYouFeel(request.POST)
        perfil = Profile()
        if request.method == 'POST':
            #request.dias_buenos = 20
            #perfil.dias_buenos += 1
            formulario = HowDoYouFeelForm(data=request.POST, instance=producto, files=request.FILES)
            #formulario = HowDoYouFeelForm(request.POST)
            #if request.POST.get("Como_estuvo_tu_dia") == 0 or request.POST.get("Como_estuvo_tu_dia") == "Bueno":
            #perfil.dias_buenos = perfil.dias_buenos +1
    #         #perfil.save()
            if formulario.is_valid():
                #formulario.data._mutable = True
                #Profile.algo = 1
                #formulario.data._mutable = False
    #         forma.user = current_user
    #         #forma.algo = request.POST
            #forma.dias_buenos += 1
                #formulario.dias_buenos += 1
                formulario.save(commit=False).total = formulario.save(commit=False).dias_buenos + formulario.save(commit=False).dias_decentes + formulario.save(commit=False).dias_normales + formulario.save(commit=False).dias_malos + formulario.save(commit=False).dias_terribles + 1
                if formulario.save(commit=False).Como_estuvo_tu_dia == 0:
                    formulario.save(commit=False).dias_buenos += 1
                    #formulario.save(commit=False).algo += "B"
                    #if formulario.save(commit=False).total != 0:
                        #formulario.save(commit=False).porcentaje_buenos = (formulario.save(commit=False).dias_buenos * 100)/formulario.save(commit=False).total
                    if formulario.save(commit=False).total == 0:
                        formulario.save(commit=False).porcentaje_buenos = 100
                
                elif formulario.save(commit=False).Como_estuvo_tu_dia == 1:
                    formulario.save(commit=False).dias_decentes += 1
                    #formulario.save(commit=False).algo += "D"
                    #if formulario.save(commit=False).total != 0:
                        #formulario.save(commit=False).porcentaje_decentes = (formulario.save(commit=False).dias_decentes * 100)/formulario.save(commit=False).total
                    if formulario.save(commit=False).total == 0:
                        formulario.save(commit=False).porcentaje_decentes = 100
                
                elif formulario.save(commit=False).Como_estuvo_tu_dia == 2:
                    formulario.save(commit=False).dias_normales += 1
                    #formulario.save(commit=False).algo += "N"
                    #if formulario.save(commit=False).total != 0:
                        #formulario.save(commit=False).porcentaje_normales = (formulario.save(commit=False).dias_normales * 100)/formulario.save(commit=False).total
                    if formulario.save(commit=False).total == 0:
                        formulario.save(commit=False).porcentaje_normales = 100

                elif formulario.save(commit=False).Como_estuvo_tu_dia == 3:
                    formulario.save(commit=False).dias_malos += 1
                    #formulario.save(commit=False).algo += "M"
                    #if formulario.save(commit=False).total != 0:
                        #formulario.save(commit=False).porcentaje_malos = (formulario.save(commit=False).dias_malos * 100)/formulario.save(commit=False).total
                    if formulario.save(commit=False).total == 0:
                        formulario.save(commit=False).porcentaje_malos = 100

                elif formulario.save(commit=False).Como_estuvo_tu_dia == 4:
                    formulario.save(commit=False).dias_terribles += 1
                    #formulario.save(commit=False).algo += "T"
                    #if formulario.save(commit=False).total != 0:
                        #formulario.save(commit=False).porcentaje_terribles = (formulario.save(commit=False).dias_terribles * 100)/formulario.save(commit=False).total
                    if formulario.save(commit=False).total == 0:
                        formulario.save(commit=False).porcentaje_terribles = 100
                if formulario.save(commit=False).total != 0:
                    formulario.save(commit=False).porcentaje_buenos = (formulario.save(commit=False).dias_buenos * 100)/formulario.save(commit=False).total
                    formulario.save(commit=False).porcentaje_decentes = (formulario.save(commit=False).dias_decentes * 100)/formulario.save(commit=False).total
                    formulario.save(commit=False).porcentaje_normales = (formulario.save(commit=False).dias_normales * 100)/formulario.save(commit=False).total
                    formulario.save(commit=False).porcentaje_malos = (formulario.save(commit=False).dias_malos * 100)/formulario.save(commit=False).total
                    formulario.save(commit=False).porcentaje_terribles = (formulario.save(commit=False).dias_terribles * 100)/formulario.save(commit=False).total
                
                #formulario.save(commit=False).algo += str(datetime.datetime.now().strftime("%Y-%m-%d")) + '&'
                #formulario.save(commit=False).total += 1
                #formulario.save(commit=False).escribe_una_palabra = formulario.save(commit=False).escribe_una_palabra.replace("$","")
                #formulario.save(commit=False).algo = formulario.save(commit=False).algo.replace("$","")
                formulario.save(commit=False).Como_estuvo_tu_dia = None
                
                if formulario.save(commit=False).algo is None:
                    formulario.save(commit=False).algo = formulario.save(commit=False).escribe_una_palabra + " "
                    formulario.save(commit=False).escribe_una_palabra = ""
                elif formulario.save(commit=False).escribe_una_palabra is None:
                    pass
                else:
                    formulario.save(commit=False).algo += str(formulario.save(commit=False).escribe_una_palabra) + " "
                    formulario.save(commit=False).escribe_una_palabra = ""
                #formulario.dias_buenos
                formulario.save()
                return redirect("http://localhost:8000/user/")
        form = HowDoYouFeelForm()
    return render(request, "app_relax/howdoyoufeel.html", data)

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

def Estadisticas(request):
    datos = Profile.objects.all()
    context = {'data': datos}
    return render(request, "app_relax/statistics.html", context)

# def modifyStatistics(request, id):
#     perfil = get_object_or_404(Profile, id=id)

#     data