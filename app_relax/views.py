from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app_relax/index.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')