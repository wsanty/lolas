from django.db import models
from productos.models import Producto


# Create your models here.

class Bodegas(models.Model):
    bodega = models.CharField(max_length=100, verbose_name="Descripcion Bodeoga")
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") 

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
        ordering = ['fecha_crea']

    def __str__(self):
        return self.bodega


class TipoMvto(models.Model):
    descripcion_mvto = models.CharField(max_length=100, verbose_name="Descripción Movimiento")
    tipo = (('E', 'Entrada'),('S', 'Salida'))
    tipomvto = models.CharField(max_length=1, choices=tipo, verbose_name="Tipo Movimiento", null=True, blank=True)
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") 
   

    class Meta:
        verbose_name = "Tipo Movimiento"
        verbose_name_plural = "Tipo Movimiento"
        ordering = ['fecha_crea']

    def __str__(self):
        return self.descripcion_mvto


class Movimiento(models.Model):
    bodega = models.ForeignKey(Bodegas, verbose_name="Bodega", null=False, blank=False, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name="Producto",null=False, blank=False, on_delete=models.CASCADE)
    tipo_mvto = models.ForeignKey(TipoMvto, verbose_name="Tipo Movimiento", null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.FloatField(verbose_name="Cantidad")
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") 


    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Registro Movimientos"
        ordering = ['fecha_crea']

    def __str__(self):
        cadena = "{0} {1} {2} --> {3}"
        return cadena.format(self.bodega, self.producto, self.tipo_mvto, self.cantidad)
