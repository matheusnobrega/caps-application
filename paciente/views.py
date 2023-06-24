from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Droga, DrogaPaciente

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
    drogas = DrogaPaciente.objects.filter(paciente__id=pk)

    return render(request, 'detalhe_paciente.html', {
        'paciente': paciente,
        'drogas': drogas,
    })

def adiciona_droga(request, pk):
    if request.method == 'POST':
        droga_id = request.POST['droga']
        idade_pu = request.POST['idade']
        frequencia = request.POST['frequencia']
        ultimo_uso = request.POST['ultimo-uso']

        droga = Droga.objects.get(pk=droga_id)
        paciente = Paciente.objects.get(pk=pk)

        droga_paciente = DrogaPaciente(droga=droga, paciente=paciente, idade_pu=idade_pu,
                                       frequencia=frequencia, ultimo_uso=ultimo_uso)
        droga_paciente.save()

        return redirect('paciente:detalhe_paciente', pk)


    drogas = Droga.objects.all()

    return render(request, 'adiciona_droga.html', {
        'drogas': drogas,
    })

def adiciona_evolucao(request, pk):

    return render(request, 'adiciona_evolucao.html')
