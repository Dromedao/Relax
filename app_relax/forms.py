from django import forms
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
import requests
from .models import HowDoYouFeel, Nota, Formulario, Dog, Profile
from tinymce.widgets import TinyMCE
#from .views import get_dog
#from .models import entrevista

class DogsForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['Name']

class Contactos(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['contactos']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class NoteForm(forms.ModelForm):
    # content = forms.CharField(label="", widget=forms.TextInput(attrs={'rows':2, 'placeholder':'¿Qué te gustaría anotar?', "class" : "ingreso-texto"}), required=True)
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué te gustaría anotar?', "class" : "ingreso-texto"}), required=True)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Nota
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'your-class'})
        }

        # widgets = {
        #     'content': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }

class SentimientoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["situation", "trigger", "sentiment", "intensity"]

class HowDoYouFeelForm(forms.ModelForm):
    class Meta:
        model = Profile
        #fields = ["Como_estuvo_tu_dia"]
        fields = ["How_was_your_day", 'Write_a_word']

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
# class Dogs(forms.ModelForm):
#     image = forms.ImageField(default=)
#     content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué te gustaría anotar?'}), required=True)
