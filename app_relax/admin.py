from django.contrib import admin
from .models import Profile, Nota, Formulario, Dog, HowDoYouFeel

# Register your models here.
admin.site.register(Profile)
admin.site.register(Nota)
admin.site.register(Formulario)
admin.site.register(Dog)
admin.site.register(HowDoYouFeel)
class PostModelAdmin(admin.ModelAdmin):
    form = Nota