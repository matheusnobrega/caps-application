from django.db import models
from django.contrib.auth.admin import User

class Servidor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    cfess = models.CharField(max_length=11)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
