from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre_completo = models.CharField(max_length=200, verbose_name="Nombre Completo")
    tipo_dcto = models.CharField(max_length=15, verbose_name="Identificación")
    correo_e = models.EmailField(verbose_name = "Correo Electrónico")
    tel_fijo = models.CharField(max_length=15, verbose_name="Fijo")
    tel_movil = models.CharField(max_length=15, verbose_name="Movil")
    direccion1 = models.CharField(max_length=40, verbose_name="Dirección")
    direccion2 = models.CharField(max_length=40, verbose_name="Dirección 2")
    ciudad = models.CharField(max_length=40, verbose_name="Ciudad")
    departamento = models.CharField(max_length=40, verbose_name="Departamento")
    pais = models.CharField(max_length=40, verbose_name="País")
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Gestión de Cliente"
        verbose_name_plural = "Gestión de Clientes"
        ordering = ['-fecha_crea']

    def __str__(self):
        return self.nombre_completo

