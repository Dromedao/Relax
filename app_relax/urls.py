from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('panic-button/', views.panic_button),
    path('about/', views.about),
    path('anxiety-tips/', views.anxiety_tips),
    path('stats/', views.stats)
]