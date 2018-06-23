from django.db import models

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(max_length=350, blank=True, null=True)
    precio_especialidad = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    class Meta:
        ordering = ['nombre_especialidad']
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidads'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.nombre_especialidad

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.nombre_especialidad