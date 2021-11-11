from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('settings/', views.settings),
    path('panic-button/', views.panic_button),
    path('user/', views.user),
    path('tips/', views.tips),
    path('stats/', views.stats)
]