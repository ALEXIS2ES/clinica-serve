from django.db import models
from .Cliente import Cliente

class Cuentausuario(models.Model):

    apellidos_clien = models.ForeignKey(Cliente, null=True, blank=True)

    codigo_usuario = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    saldo = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    fechasuscripcion_usuario = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['codigo_usuario']
        verbose_name = 'Cuentausuario'
        verbose_name_plural = 'Cuentausuarios'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.codigo_usuario

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.codigo_usuario
