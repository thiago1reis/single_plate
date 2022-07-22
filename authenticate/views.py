from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
#from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_system
from django.contrib.auth import logout as logout_system
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

# Função para fazer login.
def login(request):
    if request.method == "GET":
        return render(request, 'authenticate/login.html')
    else:
        try:
            authUsername = request.POST.get('username')
            authPassword = request.POST.get('password')
            user = authenticate(username=authUsername, password=authPassword)
            if user is not None:
                login_system(request, user)
                return redirect('sistema')
            else:
                messages.error(request, 'Usuário ou senha inválidos!')
                return redirect('login')
        except Exception as error:
            messages.error(request, error)
            return redirect('login')


# Função para direcionar ao painel do sistema.     
@login_required(login_url="/")
def sistema(request):
    return render(request, 'authenticate/painel.html')


# Função para fazer logout.
def logout(request):
    logout_system(request)
    return redirect('login')
    


