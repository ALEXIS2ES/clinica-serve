from django.db import models

# Create your models here.
# TIPODOC = (('DNI','DNI'),('RUC',RUC))


class Odontologo(models.Model):
    DNI = 'DNI'
    RUC = 'RUC'
    TIPODOC = ((DNI, 'DNI'), (RUC, 'RUC'),)
    HOMBRE = 'Hombre'
    MUJER = 'Mujer'
    GENERO = ((HOMBRE, 'Hombre'), (MUJER, 'Mujer'),)
    # ESTADO = ((0, 'Denegado'), (1, 'Activo'),)
    #nombre_odontologo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Titulo')
    apellidos_odontologo = models.CharField(max_length=50, blank=True, null=True)
    nombre_odontologo = models.CharField(max_length=50, blank=True, null=True)
    direccion_odontologo = models.CharField(max_length=50, blank=True, null=True)
    telefono_odontologo = models.CharField(max_length=9, blank=True, null=True)
    tipodoc_odontologo = models.CharField(
        max_length=10, choices=TIPODOC, default=DNI)
    numdoc_odontologo = models.IntegerField(blank=True, null=True)
    email_odontologo = models.EmailField(max_length=50, null=True)
    genero_odontologo = models.CharField(
        max_length=10, choices=GENERO, default=HOMBRE)

    # estado_cliente = models.BooleanField(default=True)
    # estado_cliente = models.IntegerField(default=1, choices=ESTADO)
    # foto = models.ImageField(upload_to='foto')

    class Meta:
        ordering = ['apellidos_odontologo']
        verbose_name = 'Odontologo'
        verbose_name_plural = 'Odontologos'

    def __unicode__(self):  # Python 2 para no mostrar "nombre object"
        return self.apellidos_odontologo

    def __str__(self):  # Python 3 para no mostrar "nombre object"
        return self.apellidos_odontologo