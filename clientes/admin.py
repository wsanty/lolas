from django.contrib import admin
from .models import Clientes

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('id','fecha_crea','fecha_actualiza')

admin.site.register(Clientes, ClienteAdmin)
