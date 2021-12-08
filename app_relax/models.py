from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.files import ImageField
from django.utils import timezone
from django.contrib.auth.models import User
from requests.api import get
from .services import get_dog
import datetime
from tinymce import models as tinymce_models

from embed_video.fields import EmbedVideoField

class Videos(models.Model):
    video = EmbedVideoField()

#from ckeditor.fields import RichTextField
# from ckeditor.fields import RichTextField

#from .services import get_dog

# Create your models here.

class Dog(models.Model):
    # context = {
    #     'message': get_dog()
    # }
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Perro')
    #imagen = ImageField(default=get_dog())
    imagen = models.CharField(max_length=200, default="")
    Name = models.CharField(default="", max_length=200)
    fecha = models.CharField(default=datetime.datetime.now().strftime("%Y-%m-%d"), max_length=200)

    def __str__(self):
        return f'Perro de {self.user.username} llamado {self.Name}'

class Profile(models.Model):
    #id = models.BigAutoField(primary_key=True)
    #id = models.PositiveIntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dias_buenos = models.IntegerField(default=0)
    porcentaje_buenos = models.FloatField(default=0)
    dias_decentes = models.IntegerField(default=0)
    porcentaje_decentes = models.FloatField(default=0)
    dias_normales = models.IntegerField(default=0)
    porcentaje_normales = models.FloatField(default=0)
    dias_malos = models.IntegerField(default=0)
    porcentaje_malos = models.FloatField(default=0)
    dias_terribles = models.IntegerField(default=0)
    porcentaje_terribles = models.FloatField(default=0)
    total = models.IntegerField(default=0)
    Write_a_word = models.CharField(max_length=1000, default="Write a word", blank=True, null=True)
    algo = models.CharField(max_length=1000, default="", blank=True, null=True)
    contactos = models.CharField(max_length=10000, default="", blank=True, null=True)

    # total_boton = models.IntegerField(default=0)

    lista_dias= [
        [0, "Good"],
        [1, "Decent"],
        [2, "Normal"],
        [3, "Bad"],
        [4, "Terrible"],
    ]
    How_was_your_day = models.IntegerField(choices=lista_dias, default=None, blank=True, null=True)

    #Formulario
    lista_sentimiento = [
        [0, "Sadness"],
        [1, "Rage"],
        [2, "Anguish"],
        [3, "Anxiety"],
        [4, "Fear"],
        [5, "Frustration"],
        [6, "Shame"],
        ]
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formulario')
    situation = models.CharField(max_length=200, default="")
    trigger = models.CharField(default="", max_length=200)
    sentiment = models.IntegerField(default=None, choices=lista_sentimiento)
    intensity = models.IntegerField(default=0, choices=[(i,i) for i in range(6)])

    total_presion = models.IntegerField(default=0)
    #Situaciones
    contador_tristeza = models.IntegerField(default=0)
    manana_tristeza = models.IntegerField(default=0)
    medioDia_tristeza = models.IntegerField(default=0)
    tarde_tristeza = models.IntegerField(default=0)
    noche_tristeza = models.IntegerField(default=0)

    contador_rabia = models.IntegerField(default=0)
    manana_rabia = models.IntegerField(default=0)
    medioDia_rabia = models.IntegerField(default=0)
    tarde_rabia = models.IntegerField(default=0)
    noche_rabia = models.IntegerField(default=0)
    
    contador_angustia = models.IntegerField(default=0)
    manana_angustia = models.IntegerField(default=0)
    medioDia_angustia = models.IntegerField(default=0)
    tarde_angustia = models.IntegerField(default=0)
    noche_angustia = models.IntegerField(default=0)

    contador_ansia = models.IntegerField(default=0)
    manana_ansia = models.IntegerField(default=0)
    medioDia_ansia = models.IntegerField(default=0)
    tarde_ansia = models.IntegerField(default=0)
    noche_ansia = models.IntegerField(default=0) 

    contador_miedo = models.IntegerField(default=0)
    manana_miedo = models.IntegerField(default=0)
    medioDia_miedo = models.IntegerField(default=0)
    tarde_miedo = models.IntegerField(default=0)
    noche_miedo = models.IntegerField(default=0) 
    
    contador_frustracion = models.IntegerField(default=0)
    manana_frustracion = models.IntegerField(default=0)
    medioDia_frustracion = models.IntegerField(default=0)
    tarde_frustracion = models.IntegerField(default=0)
    noche_frustracion = models.IntegerField(default=0) 
    
    contador_verguenza = models.IntegerField(default=0)
    manana_verguenza = models.IntegerField(default=0)
    medioDia_verguenza = models.IntegerField(default=0)
    tarde_verguenza = models.IntegerField(default=0)
    noche_verguenza = models.IntegerField(default=0) 

    porcentaje_tristeza = models.FloatField(default=0)
    porcentaje_rabia = models.FloatField(default=0)
    porcentaje_angustia = models.FloatField(default=0)
    porcentaje_ansia = models.FloatField(default=0)
    porcentaje_miedo = models.FloatField(default=0)
    porcentaje_frustracion = models.FloatField(default=0)
    porcentaje_verguenza = models.FloatField(default=0)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Nota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notas')
    timestamp = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    # content = models.CharField(default="", max_length=1000)
    #content = models.TextField()
    content = tinymce_models.HTMLField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

# class Estadisticas(models.Model):
#     veces_utilizadas = models.IntegerField()

class Formulario(models.Model):
    lista_sentimiento = [
        [0, "Tristeza"],
        [1, "Rabia"],
        [2, "Angustia"],
        [3, "Ansia"],
        [4, "Miedo"],
        [5, "Frustración"],
        [6, "Verguenza"],
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formulario')
    situacion = models.CharField(max_length=200)
    detonante = models.CharField(default="", max_length=200)
    sentimiento = models.IntegerField(default=2, choices=lista_sentimiento)
    intensidad = models.IntegerField(default=0, choices=[(i,i) for i in range(6)])

    def __str__(self):
        return f'{self.user.username}'
class HowDoYouFeel(models.Model):
    lista_dias= [
        [0, "Good"],
        [1, "Decent"],
        [2, "Normal"],
        [3, "Bad"],
        [4, "Terrible"],
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='howdoyoufeel', blank=True, null=True)
    Como_estuvo_tu_dia = models.IntegerField(choices=lista_dias)
    algo = models.CharField(max_length=10000, default = "", blank=True, null=True)
    dias = [0,0,0,0,0]

    def __str__(self):
        return f'{self.user.username}'

# class contacto(models.Model):
#     sentimiento = models.CharField(max_length=200)

# class Dogs(models.Model):
#     sentimiento = models.CharField(max_length=200)
