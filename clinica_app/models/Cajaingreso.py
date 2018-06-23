from django.db import models
from .Cuentausuario import Cuentausuario
from .Citainscripcion import Citainscripcion


class Cajaingreso(models.Model):
    ESTADO_CAJA = (
        (0, 'New'),
        (1, 'Anulado'),
        (2, 'Done'),
        (3, 'Contab'),
    )

    codigo_usuar = models.ForeignKey(Cuentausuario, null=True, blank=True)
    # serie_inscrip no sera usado, SERA USADO serie_in nombre de la funcion
    serie_inscrip = models.ManyToManyField(
        Citainscripcion, related_name='serie_i', null=True, blank=True)

    dni_pagador = models.CharField(max_length=350, blank=True, null=True)

    direccion = models.CharField(max_length=50, blank=True, null=True)
    monto = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    estado_caja = models.IntegerField(default=2, choices=ESTADO_CAJA)

    def serie_in(self):  # este nombre va para admin y serializaer
        return ",".join([str(p) for p in self.serie_inscrip.all()])

    class Meta:
        verbose_name = "Cajaingreso"
        verbose_name_plural = "Cajaingresos"

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.dni_pagador

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.dni_pagador
