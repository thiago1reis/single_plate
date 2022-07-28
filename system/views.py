from cmath import e
import random
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from system.forms import OwnerForm
from system.models import Owner, Plate
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
def owner_delete(request, owner_pk):
    owner = Owner.objects.get(pk=owner_pk)
    owner.delete()
    messages.success(request, 'Propietário deletado com sucesso!')
    return redirect('owner_index') 

######################################## VIEWS DE PLACAS ######################################## 

# view para listar todas as placas.
@login_required(login_url="/")
def plate_index(request):
    plates = Plate.objects.all().order_by('-created')
    paginator = Paginator(plates, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'system/plate_index.html', context)

# view para gerar uma placa.    
@login_required(login_url="/")
def plate_add(request):
    if request.method == "GET":
        owners = Owner.objects.all().order_by('name')
        context = {
            'owners' : owners,
        }
        return render(request, 'system/plate_add.html', context)
    else:
        try: 
            plate = Plate()
            plate.state = request.POST.get('state')
            plate.type = request.POST.get('type')
            #gera as três primeira letras a placa
            plate.three_char = chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z')))
            #gera o primero número da placa  
            plate.only_number = int(chr(random.randint(ord('0'), ord('9'))))
            #gera a última letra da placa (essa fica entre os numeros)
            plate.single_char = chr(random.randint(ord('a'), ord('z')))
            #gera os dois últimos numeros da placa
            plate.two_number = int(chr(random.randint(ord('0'), ord('9'))) + chr(random.randint(ord('0'), ord('9')))) 
            plate.status = True
            plate.owner = Owner.objects.get(pk=request.POST.get('owner_id'))
            plate.save()
            messages.success(request, 'Placa gerada com sucesso!')
            return redirect('plate_index')
        except Exception as error:
            owners = Owner.objects.all().order_by('name')
            context = {
                'owners' : owners,
            }
            messages.error(request, error)
            return render(request, 'system/plate_add.html', context,) 

# view para editar uma placa. 
@login_required(login_url="/")
def plate_edit(request, plate_pk):
    if request.method == "GET":
        plate = Plate.objects.get(pk=plate_pk)
        context = {
            'plate': plate
        }
        return render(request, 'system/plate_edit.html', context)
    else:
        try:
            plate = Plate.objects.get(pk=plate_pk)
            if request.POST.get('status'): 
                plate.status = True 
            else:
                plate.status = False  
            plate.state = request.POST.get('state')
            plate.type = request.POST.get('type')
            plate.save()
            messages.success(request, 'Dados da placa editados com sucesso!')
            return redirect('plate_index')
        except Exception as error:
            plate = Plate.objects.get(pk=plate_pk)
            context = {
                'plate': plate
            }
            messages.error(request, error)
            return render(request, 'system/plate_edit.html', context)

# view para deletar um propietário.
@login_required(login_url="/")
def plate_delete(request, plate_pk):
    plate = Plate.objects.get(pk=plate_pk)
    plate.delete()
    messages.success(request, 'Placa deletada com sucesso!')
    return redirect('plate_index')             
               
######################################## VIEWS DE VEÍCULOS ########################################     



      
