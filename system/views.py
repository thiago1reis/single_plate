from cmath import e
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from system.forms import OwnerForm
from system.models import Owner
# Create your views here.

# Função para listar todos os propietários.
@login_required(login_url="/")
def owner_index(request):
    owners = Owner.objects.all()
    context = {
        'owners': owners
    }
    return render(request, 'system/owner_index.html', context)

# Função para adicionar novos propietários.
@login_required(login_url="/")
def owner_add(request):
    form = OwnerForm(request.POST or None)
    try:
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Propietário adicionado com sucesso!')
                return redirect('owner_index')
    except Exception as error:
        messages.error(request, error)
        return redirect('owner_add')
    context = {'form': form }
    return render(request, 'system/owner_add.html', context)


# #Função para editar um propietários.
# def owner_index(request):
#     return HttpResponse('lista dos propietarios')



      
