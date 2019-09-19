from django.urls import path
from .views import Lista, Cadastrar, index

urlpatterns = [
    path('', index),
    path('listar', Lista.as_view(), name='listar'),
    path('cadastro', Cadastrar.as_view(), name='cadastrar'),
]
