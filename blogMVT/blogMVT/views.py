from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def saludo(request):

    plantilla = loader.get_template('index.html')
    
    return HttpResponse("Hola :D")

def index(request):

    return render(request, 'blogAPP/index.html')

    