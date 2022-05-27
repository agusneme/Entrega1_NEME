from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('camada', views.camada, name="Camada"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),


]