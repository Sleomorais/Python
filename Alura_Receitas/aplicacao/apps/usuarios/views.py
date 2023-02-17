from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth,messages
from receitas.models import Receita

def cadastro(request):
    """CADASTRA UMA NOVA PESSOA NO SISTEMA"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'campo de nome está inválido')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'campo de email está inválido')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha,senha2):
            messages.error(request, 'campos de senha contém informações diferentes')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error('usuario já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error('usuario já cadastrado')
            return redirect('cadastro')
            

        user = User.objects.create_user(username=nome, email = email, password= senha)
        user.save()
        print('usuario cadastrado')
        messages.success(request, 'Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """REALIZA O LOGIN DO USUARIO NO SISTEMA"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request,'campo vazio')
            return redirect('login')
        print(email,senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username= nome, password= senha)
            if user is not None:
                auth.login(request, user)
                print('Login feito com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')
def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receita = Receita.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas' : receita
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
def campo_vazio(campo):
    return not campo.strip()
def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2