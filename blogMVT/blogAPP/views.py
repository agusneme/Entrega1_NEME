from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from blogAPP.models import Curso, Profesor, Estudiante
from blogAPP.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario


# Create your views here.
def inicio(request):

      return render(request, "blogAPP/inicio.html")

def estudiantes(request):

      return render(request, "blogAPP/estudiantes.html")

def camada(request):

        return render(request, 'blogAPP/camada.html')

def profesores(request):
        return render(request, 'blogAPP/profesores.html')