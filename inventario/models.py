from django.db import models

# Create your models here.

class Entradas(models.Model):
    documento =
    consecutivo =
    fecha_ent =
    notas =
    producto =
    concepto =
    cantidad =

 class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['fecha_ent']

    def __str__(self):
        return self.tipo_mvto,

class MovimientoInv(models.Model):
    tipo_mvto = 
    fecha_mvto =
    producto =
    cant_ent =
    cant_sal =
    costo_uni =
    costo_total = 


    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        ordering = ['fecha_mvto']

    def __str__(self):
        return self.tipo_mvto, self.fecha_mvto, self.producto, self.cant_ent, self.cant_sal
