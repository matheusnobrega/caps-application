from django.db import models

class UnidadeAcolhimento(models.Model):
    num_leitos = models.IntegerField()
    qtd_disponivel = models.IntegerField()
