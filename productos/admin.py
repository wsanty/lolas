from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')
    list_display = ('id','nombre','tipo','estado','fecha_crea')
    search_fields = ('nombre',)
    ordering = ('id',)

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
