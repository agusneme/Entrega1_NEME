from django.urls import path
from blogAPP import views
from .views import index

urlpatterns = [

    path('', views.index, name="index"),

]