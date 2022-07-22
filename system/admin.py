from django.contrib import admin
from .models import Address, Owner, Plate, Vehicle, Register

# Register your models here.
admin.site.register(Address)
admin.site.register(Owner)
admin.site.register(Plate)
admin.site.register(Vehicle)
admin.site.register(Register)

