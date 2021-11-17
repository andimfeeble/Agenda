#from django.db import models
#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contato

#def index(request):
#    return HttpResponse('Olá, este é meu primeiro App!')

class ContatoListView(ListView):
    model = Contato

class ContatoDetailView(DetailView):
    model = Contato