from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class contacto(models.Model):
    sentimiento = models.CharField(max_length=200)
    