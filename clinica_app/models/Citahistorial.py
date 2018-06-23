from django.db import models
from .Citainscripcion import Citainscripcion
from .Especialidad import Especialidad

class Citahistorial(models.Model):
    #seri para id y serie para mostrar seri
    serie_inscrip = models.ForeignKey(Citainscripcion, null=True, blank=True)
    serie = models.CharField(max_length=350, blank=True, null=True)

    fecha_atencion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    nombre_especiali = models.ForeignKey(Especialidad, null=True, blank=True)

    fecha_atender = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(max_length=350, blank=True, null=True)

    precio_un = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "Citahistorial"
        verbose_name_plural = "Citahistorials"

    def __str__(self):
        return self.serie