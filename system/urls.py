from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('propietarios', views.owner_index, name='owner_index'),   
    # path('sistema', views.sistema, name="sistema"),
    # path('logout', views.logout, name="logout"),
] 