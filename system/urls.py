from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    #urls propietários
    path('propietarios', views.owner_index, name='owner_index'),   
    path('propietario/novo', views.owner_add, name="owner_add"),
    path('propietario/visualizar/<int:owner_pk>', views.owner_show, name='owner_show'),
    path('propietario/editar/<int:owner_pk>', views.owner_edit, name='owner_edit'),
    path('propietario/deletar/<int:owner_pk>', views.owner_delete, name='owner_delete'),
    #urls placas
    path('placas', views.plate_index, name='plate_index'),   
    path('placa/gerar', views.plate_add, name="plate_add"),
    path('placa/editar/<int:plate_pk>', views.plate_edit, name='plate_edit'),
    path('placa/deletar/<int:plate_pk>', views.plate_delete, name='plate_delete'), 
    #urls veículos
    path('veiculos', views.vehicle_index, name='vehicle_index'),    
    path('veiculo/novo', views.vehicle_add, name="vehicle_add"),
    path('veiculo/editar/<int:vehicle_pk>', views.vehicle_edit, name='vehicle_edit'),
    path('veiculo/deletar/<int:vehicle_pk>', views.vehicle_delete, name='vehicle_delete'),
] 
 