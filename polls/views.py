# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo!")

def sobre(request):
    return HttpResponse("Esta é a página sobre do meu site.")