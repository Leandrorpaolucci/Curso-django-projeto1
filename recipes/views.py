from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse('Contato 1')

def sobre(request):
    return HttpResponse('Sobre')