from cmath import e
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from system.forms import OwnerForm
from system.models import Owner
from django.core.paginator import Paginator

######################################## VIEWS DE PROPIETÁRIOS ########################################

# view para listar todos os propietários.
@login_required(login_url="/")
def owner_index(request):
    owners = Owner.objects.all().order_by('-created')
    paginator = Paginator(owners, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'system/owner_index.html', context)

# view para adicionar novos propietários. 
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

# view para visualizar dados de um propietário.
@login_required(login_url="/")
def owner_show(request, owner_pk):
    owner = Owner.objects.get(pk=owner_pk)
    context = {
            'owner': owner
        }
    return render(request, 'system/owner_show.html', context,)  

# view para editar um propietário.
@login_required(login_url="/")
def owner_edit(request, owner_pk):
    owner = Owner.objects.get(pk=owner_pk)
    form = OwnerForm(request.POST or None, instance=owner)
    try:
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados do propietário editado com sucesso!')
                return redirect('owner_index')   
    except Exception as error:
        context = {
            'form': form,
            'owner': owner.id
        }
        messages.error(request, error)
        return render(request, 'system/owner_edit.html', context,)             
    context = {
        'form': form,
        'owner': owner.id
    }
    return render(request, 'system/owner_edit.html', context,)        

# view para deletar um propietário.
@login_required(login_url="/")
def autor_delete(request, owner_pk):
    owner = Owner.objects.get(pk=owner_pk)
    owner.delete()
    messages.success(request, 'Propietário deletado com sucesso!')
    return redirect('owner_index') 

######################################## VIEWS DE PLACAS ######################################## 
# view para deletar um propietário.    
@login_required(login_url="/")
def plate_add(request):
    owners = Owner.objects.all().order_by('-name')
    context = {
        'owners' : owners
    }
    return render(request, 'system/plate_add.html', context)
    



      
