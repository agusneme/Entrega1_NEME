from django.urls import path
from blogAPP import views

urlpatterns = [

    path('index', views.index, name="index"),

]