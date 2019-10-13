from django.contrib import admin
from .models import Vehiculo, Cliente, Proveedor, Articulo, Ficha_Tecnica, Reparacion

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('cliente', 'matricula', 'marca', 'modelo')

admin.site.register(Vehiculo, VehiculoAdmin)

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Articulo)
admin.site.register(Ficha_Tecnica)
admin.site.register(Reparacion)

