from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from medico.models import Medico
from servidor.models import Servidor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def vw_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        nome_usuario = request.POST['nome-usuario']
        senha = request.POST['senha']

        user = authenticate(request, username=nome_usuario, password=senha)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            return HttpResponse('Erro na realização do login')
        
    return render(request, 'login.html')

def vw_logout(request):
    logout(request)
    return redirect('index')

def vw_register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['CPF']
        nome_usuario = request.POST['nome-usuario']
        primeira_senha = request.POST['primeira-senha']
        segunda_senha = request.POST['segunda-senha']
        funcao = request.POST['funcao']
        

        if primeira_senha != segunda_senha:
            return HttpResponse('Senhas não equivalem')
        
        if len(cpf) != 11:
            return HttpResponse('CPF inválido')
        
        if len(nome_usuario) < 4:
            return HttpResponse('Nome de usuário muito curto')
        
        usuario = User.objects.create_user(username=nome_usuario, password=primeira_senha)
        
        if funcao == 'servidor':
            cress = request.POST['CRESS']
            servidor = Servidor(nome=nome, cpf=cpf, cfess=cress, usuario=usuario)
            servidor.save()

        else:
            crm = request.POST['CRM']
            medico = Medico(nome=nome, cpf=cpf, crm=crm, usuario=usuario)
            medico.save()


        login(request, usuario)
        return redirect('index')

    return render(request, 'register.html')

