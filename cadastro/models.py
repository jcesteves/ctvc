from django.db import models
from django.urls import reverse


class CadastroModel(models.Model):
    DATA_REG = models.DateTimeField(auto_now_add=True)
    CENTRO_CUSTO = models.CharField(max_length=15)
    OPERACAO = models.CharField(max_length=100)
    NOME_TECNICO = models.CharField(max_length=200)
    ATIVIDADE = models.TextField()
    CELULAR_CORPORATIVO = models.CharField(max_length=11)
    CELULAR_PESSOAL = models.CharField(max_length=11)
    TELEFONE_RESIDENCIA = models.CharField(max_length=11)
    ENDERECO_RESIDENCIA = models.CharField(max_length=11)
    CIDADE = models.CharField(max_length=20)
    UF = models.CharField(max_length=2)
    #Coluna2
    ESCALA_HORARIO = models.TimeField(auto_now=True)
    TIPO_VEICULO = models.CharField(max_length=15)
    MARCA_VEICULO = models.CharField(max_length=15)
    MODELO_VEICULO = models.CharField(max_length=15)
    PLACA_VEICULO = models.CharField(max_length=7, unique=True)
    CARTAO_VALE = models.CharField(max_length=20, unique=True)
    CARD = models.CharField(max_length=20, unique=True)
    RG = models.CharField(max_length=10, unique=True)
    CPF = models.CharField(max_length=11, unique=True)
    HABILITACAO =  models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.NOME_TECNICO

    def get_absolute_url(self):
        return reverse('listar')
