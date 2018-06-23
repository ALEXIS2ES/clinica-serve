from django.contrib import admin

# Register your models here.
from .models.Cajaingreso import Cajaingreso
from .models.Citahistorial import Citahistorial
from .models.Citainscripcion import Citainscripcion
from .models.Cliente import Cliente
from .models.Cuentausuario import Cuentausuario
from .models.Especialidad import Especialidad
from .models.Odontologo import Odontologo


class CajaingresoAdmin(admin.ModelAdmin):
    list_per_page = 5
    # list_display = ["codigo_usuar", "cita_i", "direccion",
    #"monto", "fecha", "estado_caja"]
    #list_editable = ["monto", "estado_caja"]
    #search_fields = ["codigo_usuar", "fecha"]

    list_display = ["serie_in", "codigo_usuar", "dni_pagador", "direccion", "monto",
                    "fecha", "estado_caja"]
    search_fields = ["dni_pagador"]
    #list_filter = ("codigo_usuar",)


class CitahistorialAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["serie", "fecha_atencion", "nombre_especiali",
                    "fecha_atender", "descripcion", "precio_un", "cantidad"]
    #list_display_links = ["seri"]
    # list_editable = ["nombre_especiali", "fecha_atender",
    #"descripcion", "precio_un", "cantidad"]
    search_fields = ["serie"]


class CitainscripcionAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["apellidos_clien", "apellidos_odonto", "serie", "ruc", "tipo_pago", "tipodocumento_pago",
                    "direccion", "fecha_citasuscripcion", "fecha_citaatender"]
    list_editable = ["tipo_pago", "tipodocumento_pago",
                     "fecha_citaatender"]
    search_fields = ["serie"]


class ClienteAdmin(admin.ModelAdmin):
    list_per_page = 5
   # list_display = ("apellidos_paciente", "nombre_paciente")
    list_display = ["apellidos_cliente", "nombre_cliente", "direccion_cliente", "telefono_cliente",
                    "tipodoc_cliente", "numdoc_cliente", "email_cliente", "genero_cliente", "fechasuscripcion_cliente"]
    list_display_links = ["apellidos_cliente", "nombre_cliente"]
    list_editable = ["direccion_cliente", "telefono_cliente", "email_cliente"]
    search_fields = ["apellidos_cliente", "nombre_cliente"]

    # class Meta:
    #    model = Cliente


class CuentausuarioAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["apellidos_clien", "codigo_usuario",
                    "password", "saldo", "fechasuscripcion_usuario"]
    list_display_links = ["apellidos_clien"]
    list_editable = ["password", "saldo"]
    search_fields = ["codigo_usuario"]


class EspecialidadAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["nombre_especialidad",
                    "descripcion", "precio_especialidad"]
    list_display_links = ["nombre_especialidad"]
    list_editable = ["descripcion", "precio_especialidad"]
    search_fields = ["nombre_especialidad"]


class OdontologoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["apellidos_odontologo", "nombre_odontologo", "direccion_odontologo", "telefono_odontologo",
                    "tipodoc_odontologo", "numdoc_odontologo", "email_odontologo", "genero_odontologo"]
    list_display_links = ["apellidos_odontologo", "nombre_odontologo"]
    list_editable = ["direccion_odontologo",
                     "telefono_odontologo", "email_odontologo"]
    search_fields = ["apellidos_odontologo", "nombre_odontologo"]


admin.site.register(Cajaingreso, CajaingresoAdmin)
admin.site.register(Citahistorial, CitahistorialAdmin)
admin.site.register(Citainscripcion, CitainscripcionAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cuentausuario, CuentausuarioAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Odontologo, OdontologoAdmin)
