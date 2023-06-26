from django.db import models
from servidor.models import Servidor
from unidade_acolhimento.models import UnidadeAcolhimento


class Droga(models.Model):
    nome = models.CharField(max_length=150)

class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.CharField(max_length=150, null=True, blank=True)
    sexo = models.BooleanField(null=True, blank=True)
    identidade_genero = models.CharField(max_length=50, null=True, blank=True)
    filiacao = models.CharField(max_length=50, null=True, blank=True)
    naturalidade = models.CharField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)
    rg = models.CharField(max_length=50, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    cns = models.CharField(max_length=50, null=True, blank=True)
    situacao_rua = models.BooleanField(null=True, blank=True)
    drogas = models.ManyToManyField(Droga, through='DrogaPaciente', blank=True)
    unidade_acolhimento = models.ForeignKey(UnidadeAcolhimento, null=True, blank=True, on_delete=models.SET_NULL)


class DrogaPaciente(models.Model):
    droga = models.ForeignKey(Droga, related_name='droga', on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, related_name='paciente', on_delete=models.CASCADE)
    idade_pu = models.IntegerField()
    frequencia = models.CharField(max_length=30)
    ultimo_uso = models.DateField()

class Evolucao(models.Model):
    descritivo = models.CharField(max_length=150)
    data = models.DateField()
    paciente = models.ForeignKey(Paciente, related_name='pacientes', on_delete=models.CASCADE)
    servidor = models.ForeignKey(Servidor, related_name='servidores', on_delete=models.CASCADE)


