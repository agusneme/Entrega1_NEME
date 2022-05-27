from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, 'blogAPP/index.html')

