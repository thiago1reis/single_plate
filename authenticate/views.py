from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_system
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'authenticate/login.html')
    else:
        authUsername = request.POST.get('username')
        authPassword = request.POST.get('password')
        user = authenticate(username=authUsername, password=authPassword)
        if user is not None:
            login_system(request, user)
           
            return redirect('login')
        else:
            return HttpResponse('Email ou Senha Inválidos')


@login_required(login_url="/")
def sistema(request):
    return HttpResponse('Bem vindo ao painel de controle!')
    


