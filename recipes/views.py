# A função render tem como objetivo renderizar um arquivo html dentro de uma função
from django.shortcuts import render


from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')