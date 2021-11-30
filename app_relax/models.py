from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
#from .services import get_dog

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Nota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notas')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

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

# class contacto(models.Model):
#     sentimiento = models.CharField(max_length=200)

# class Dogs(models.Model):
#     sentimiento = models.CharField(max_length=200)
