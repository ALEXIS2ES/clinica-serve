from django.db import models
from .Cliente import Cliente
from .Odontologo import Odontologo

class Citainscripcion(models.Model):
    ESTADO_CITA = (
        (0, 'New'),
        (1, 'Anulado'),
        (2, 'Done'),
        (3, 'Contab'),
    )
    FACTURA = 'Factura'
    BOLETA = 'Boleta'
    TICKET = 'Ticket'
    TIPO_DOC = (
        (FACTURA, 'Factura'),
        (BOLETA, 'Boleta'),
        (TICKET, 'Ticket'),
    )
    EFECTIVO = 'Efectivo'
    CUOTAS = 'Cuotas'
    TIPO_PAGO = (
        (EFECTIVO, 'Efectivo'),
        (CUOTAS, 'Cuotas'),
    )
    apellidos_clien = models.ForeignKey(Cliente, null=True, blank=True)
    apellidos_odonto = models.ForeignKey(Odontologo, null=True, blank=True)

    serie = models.CharField(max_length=50, blank=True, null=True)
    ruc = models.CharField(max_length=50, blank=True, null=True)
    tipo_pago = models.CharField(max_length=10, choices=TIPO_PAGO, default=EFECTIVO)
    tipodocumento_pago = models.CharField(max_length=10, choices=TIPO_DOC, default=TICKET)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    fecha_citasuscripcion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_citaatender = models.DateTimeField(blank=True, null=True)
    #estado_cita = models.IntegerField(default=2, choices=ESTADO_CITA)
    #estado_cita = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Citainscripcion"
        verbose_name_plural = "Citainscripcions"

    def __str__(self):
        return self.serie
        