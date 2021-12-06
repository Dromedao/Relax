from re import template
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.home),
    path('settings/', views.settings),
    path('panic-button/', views.panic_button),
    path('user/', views.user),
    path('tips/', views.tips),
    path('stats/', views.stats),
    path('notes/', views.notes),
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="app_relax/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="app_relax/logout.html"), name="logout"),
    path("newnotes/", views.nota, name="nota"),
    path("dogs/", views.hello_user),
    path("formulario/", views.FormularioView),
    path("owndogs/", views.MostrarPerros),
    path("player/", views.mp3player),
    path("statistics/", views.Estadisticas),
    path("howdoyoufeel/", views.HowDoYouFeelView),
    path('tinymce/', include('tinymce.urls')),
    path("paint/", views.paint)
]