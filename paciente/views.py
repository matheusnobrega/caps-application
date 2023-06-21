from django.shortcuts import render
from .models import Paciente

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
