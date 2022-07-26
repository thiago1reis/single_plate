from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('propietarios', views.owner_index, name='owner_index'),   
    path('propietario/novo', views.owner_add, name="owner_add"),
    path('propietario/visualizar/<int:owner_pk>', views.owner_show, name='owner_show'),
    path('propietario/editar/<int:owner_pk>', views.owner_edit, name='owner_edit'),
    path('propietario/deletar/<int:owner_pk>', views.autor_delete, name='owner_delete'),
    path('placas', views.plate_index, name='plate_index'),   
    path('placa/gerar', views.plate_add, name="plate_add"), 
] 
