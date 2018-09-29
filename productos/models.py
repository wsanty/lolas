from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = nombre = models.CharField(max_length=100, verbose_name="Categoria")
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    tpo = (('P', 'Producto'),('S','Servicio'))
    tipo = models.CharField(max_length=1, choices=tpo, verbose_name="Tipo", null=True, blank=True)
    categoria =  models.ManyToManyField('Categoria', verbose_name="Categoría del Producto")
    costo = models.FloatField(verbose_name="Costo")
    precio = models.FloatField(verbose_name="Precio")
    notas = models.TextField(verbose_name="Notas", null=True, blank=True)
    est = (('A', 'Activo'),('I', 'Inactivo'))
    estado = models.CharField(max_length=1, choices=est, verbose_name="Estado", null=True, blank=True)
    fecha_crea = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualiza = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre