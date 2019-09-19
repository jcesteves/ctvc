from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import CadastroModel


def index(request):
    return render(request, 'html/base.html')

class Lista(ListView):
    model = CadastroModel


class Cadastrar(CreateView):
    model = CadastroModel
    fields = '__all__'

    def get_absolute_url(self):
        return reverse('listar')

