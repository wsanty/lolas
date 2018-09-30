from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
