from django.contrib import admin
from .models import Bodegas, TipoMvto, Movimiento

# Register your models here.
class BodegasAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

class TipoMvtoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

class MovimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')


admin.site.register(Bodegas, BodegasAdmin)
admin.site.register(TipoMvto, TipoMvtoAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
