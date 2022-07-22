from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from system.models import Address, Owner
# Create your views here.

# Função para listar todos os propietários.
def owner_index(request):
    return HttpResponse('lista dos propietarios')


# Função para adicionar novos propietários.
def owner_add(request):
    if request.method == "GET":
        return render(request, 'system/owner_add.html')
    else:
        try:
            number = ""
            complement = ""
            reference_point = ""
            if request.POST.get('number'): number =  request.POST.get('number')  
            if request.POST.get('complement'): complement =  request.POST.get('number')  
            if request.POST.get('reference_point'): reference_point =  request.POST.get('reference_point') 

            address = Address.objects.create(
                zip_code = request.POST.get('zip_code'),
                state = request.POST.get('state'),
                city = request.POST.get('city'),
                district = request.POST.get('district'),
                road = request.POST.get('road'),
                number = number,
                complement = complement,
                reference_point = reference_point
            )

            email = "",
            telephone = "",
            comments = "",
            if request.POST.get('email'): email =  request.POST.get('email')  
            if request.POST.get('telephone'): telephone =  request.POST.get('telephone')  
            if request.POST.get('comments'): comments =  request.POST.get('comments') 

            Owner.objects.create(
                name = request.POST.get('name'),
                birth_date =request.POST.get('birth_date'),
                sex = request.POST.get('sex'),
                cpf = request.POST.get('cpf'),
                telephone = telephone,
                email = email,
                comments = comments,
                address_id = address.id
            ) 
            messages.success(request, 'Propietário adicionado com sucesso!')
            return redirect('owner_add')
        except Exception as error:
            messages.error(request, error)
            return redirect('owner_add')


# Função para editar um propietários.
# def owner_index(request):
#     return HttpResponse('lista dos propietarios')



      
