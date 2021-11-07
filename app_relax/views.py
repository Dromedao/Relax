from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app_relax/index.html')

def products(request):
    return HttpResponse('products')

def panic_button(request):
    return render(request, 'app_relax/panic-button.html')

def about(request):
    return render(request, 'app_relax/about.html')

def anxiety_tips(request):
    return render(request, 'app_relax/anxiety-tips.html')

def stats(request):
    return render(request, 'app_relax/stats.html')