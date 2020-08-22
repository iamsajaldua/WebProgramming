from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Welcome to PALO ALTO!")

def sajal(request):
    return HttpResponse("Hello, Sajal!")

def zidane(request):
    return HttpResponse("Hello, zidane")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")