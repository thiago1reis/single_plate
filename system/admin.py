from django.contrib import admin
from .models import Owner, Plate, Vehicle, Register

# Register your models here.
admin.site.register(Owner)
admin.site.register(Plate)
admin.site.register(Vehicle)
admin.site.register(Register)

