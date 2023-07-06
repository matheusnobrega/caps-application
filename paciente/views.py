from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Droga, DrogaPaciente, Evolucao
from unidade_acolhimento.models import UnidadeAcolhimento
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    data_nascimento = paciente.data_nascimento.strftime('%Y-%m-%d')

    if request.method == 'POST':
        paciente.nome = request.POST['nome']
        paciente.data_nascimento = request.POST['data-nascimento']
        paciente.endereco = request.POST['endereco']
        paciente.sexo = request.POST['sexo']
        paciente.identidade_genero = request.POST['identidade-genero']
        paciente.filiacao = request.POST['filiacao']
        paciente.endereco = request.POST['endereco']
        paciente.naturalidade = request.POST['naturalidade']
        paciente.telefone = request.POST['telefone']
        paciente.cpf = request.POST['cpf']
        paciente.cns = request.POST['cns']
        paciente.situacao_rua = request.POST['situacao-rua']
        paciente.save()

        return HttpResponseRedirect(reverse('paciente:detalhe_paciente', args=[paciente.id]))

    return render(request, 'atualiza_paciente.html', {
        'paciente': paciente,
        'data_nascimento': data_nascimento,
    })

def listar_pacientes(request):
    pacientes =  Paciente.objects.all()

    return render(request, 'lista_pacientes.html', {
        'pacientes': pacientes,
    })

def detalhe_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    drogas = DrogaPaciente.objects.filter(paciente__id=pk)
    evolucoes = Evolucao.objects.filter(paciente__id=pk)

    return render(request, 'detalhe_paciente.html', {
        'paciente': paciente,
        'drogas': drogas,
        'evolucoes': evolucoes,
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

def remove_droga(request, pk, dp_pk):
    droga_paciente = get_object_or_404(DrogaPaciente, pk=dp_pk)

    if request.method == 'POST':
        droga_paciente.delete()

        return redirect('paciente:detalhe_paciente', pk)

def adiciona_evolucao(request, pk):

    if request.method == 'POST':
        descritivo = request.POST['descricao']

        data = date.today()
        usuario = request.user
        servidor = usuario.servidor
        paciente = Paciente.objects.get(pk=pk)

        evolucao = Evolucao(descritivo=descritivo, data=data,
                            paciente=paciente, servidor=servidor)
        evolucao.save()

        return redirect('paciente:detalhe_paciente', pk)


    return render(request, 'adiciona_evolucao.html')

def insere_unidade_acolhimento(request, pk):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk=pk)
        unidade_acolhimento = UnidadeAcolhimento.objects.filter().first()

        paciente.unidade_acolhimento = unidade_acolhimento
        paciente.save()

        return redirect('paciente:detalhe_paciente', pk)
    
def remove_unidade_acolhimento(request, pk):
    if request.method == 'POST':
        paciente = get_object_or_404(Paciente, pk=pk)

        paciente.unidade_acolhimento = None
        paciente.save()

        return redirect('paciente:detalhe_paciente', pk)
    
def apresenta_estatisticas(request):
    consumo_drogas = DrogaPaciente.objects.all()
    pacientes = Paciente.objects.all()

    total_masculino = pacientes.filter(sexo=False).count()
    total_feminino = pacientes.filter(sexo=True).count()

    labels_sexo = ['Masculino', 'Feminino']
    data_sexo = [total_masculino, total_feminino]

    drogas = {}

    for consumo in consumo_drogas:
        droga = consumo.droga.nome
        if droga in drogas:
            drogas[droga] += 1
        else:
            drogas[droga] = 1

    labels = list(drogas.keys())
    data = list(drogas.values())
    
    print(labels, data)

    return render(request, 'apresenta_estatisticas.html', {
        'labels': labels,
        'data': data,
        'labels_sexo': labels_sexo,
        'data_sexo': data_sexo,
    })
