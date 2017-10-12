from django.contrib import admin

# Register your models here.
from .models import Marcas,Vehiculo,TiposCombustibles,TiposVehiculos,Modelos,Clientes,Empleados,Rerservaciones

admin.site.register(Marcas)
admin.site.register(Vehiculo)
admin.site.register(TiposCombustibles)
admin.site.register(TiposVehiculos)
admin.site.register(Modelos)
admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Rerservaciones)


