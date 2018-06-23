from django.db import models

# Create your models here.
# TIPODOC = (('DNI','DNI'),('RUC',RUC))


class Cliente(models.Model):
    DNI = 'DNI'
    RUC = 'RUC'
    TIPODOC = ((DNI, 'DNI'), (RUC, 'RUC'),)
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENERO = ((HOMBRE, 'Hombre'), (MUJER, 'Mujer'),)
    # ESTADO = ((0, 'Denegado'), (1, 'Activo'),)
    #nombre_cliente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    apellidos_cliente = models.CharField(max_length=50, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=50, blank=True, null=True)
    direccion_cliente = models.CharField(max_length=50, blank=True, null=True)
    telefono_cliente = models.CharField(max_length=9, blank=True, null=True)
    tipodoc_cliente = models.CharField(
        max_length=10, choices=TIPODOC, default=DNI)
    numdoc_cliente = models.IntegerField(blank=True, null=True)
    email_cliente = models.EmailField(max_length=50, null=True)
    genero_cliente = models.CharField(
        max_length=10, choices=GENERO, default=HOMBRE)
    fechasuscripcion_cliente = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    # estado_cliente = models.BooleanField(default=True)
    # estado_cliente = models.IntegerField(default=1, choices=ESTADO)
    # foto = models.ImageField(upload_to='foto')

    class Meta:
        ordering = ['apellidos_cliente']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.apellidos_cliente

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.apellidos_cliente
