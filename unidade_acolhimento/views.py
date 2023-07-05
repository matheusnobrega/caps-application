from django.shortcuts import render
from paciente.models import Paciente
from .models import UnidadeAcolhimento

def detalhe_unidade(request):
    unidade_acolhimento = UnidadeAcolhimento.objects.filter().first()
    pacientes = Paciente.objects.exclude(unidade_acolhimento__isnull=True)

    vagas_ocupadas = pacientes.count()

    return render(request, 'detalhe_unidade.html', {
        'pacientes': pacientes,
        'vagas_ocupadas': vagas_ocupadas,
        'unidade_acolhimento': unidade_acolhimento,
    })
