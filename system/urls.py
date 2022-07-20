from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('propietarios', views.owner_index, name='owner_index'),   
    path('propietario/novo', views.owner_add, name="owner_add"),
    # path('logout', views.logout, name="logout"),
] 