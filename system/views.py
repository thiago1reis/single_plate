from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def owner_index(request):
    return HttpResponse('lista dos propietarios')

def owner_add(request):
    return HttpResponse('lista dos propietarios')
