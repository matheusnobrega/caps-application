from django.shortcuts import render, get_object_or_404
from .models import Paciente, Droga

def cadastrar_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nasc = request.POST['data-nascimento']
        endereco = request.POST['endereco']
        sexo = request.POST['sexo']
        identidade_genero = request.POST['identidade-genero']
        filiacao = request.POST['filiacao']
        endereco = request.POST['endereco']
        naturalidade = request.POST['naturalidade']
        telefone = request.POST['telefone']
        cpf = request.POST['cpf']
        cns = request.POST['cns']
        situacao_rua = request.POST['situacao-rua']

        novo_paciente = Paciente(nome=nome, data_nascimento=data_nasc, endereco=endereco,
                            sexo=sexo, identidade_genero=identidade_genero, filiacao=filiacao,
                            naturalidade=naturalidade, telefone=telefone, cpf=cpf,
                            cns=cns)
        novo_paciente.save()
        

    return render(request, 'insere_paciente.html')

def listar_pacientes(request):
    pacientes =  Paciente.objects.all()

    return render(request, 'lista_pacientes.html', {
        'pacientes': pacientes,
    })

def detalhe_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    return render(request, 'detalhe_paciente.html', {
        'paciente': paciente
    })

def adiciona_droga(request, pk):
    drogas = Droga.objects.all()

    return render(request, 'adiciona_droga.html', {
        'drogas': drogas,
    })
