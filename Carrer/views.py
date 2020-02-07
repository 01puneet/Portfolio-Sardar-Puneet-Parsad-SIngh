from django.shortcuts import render
from .models import Carrer

def home(request):
    carrers = Carrer.objects
    return  render(request, 'carrer/home.html', {'carrers': carrers})
