from rest_framework import serializers, viewsets, routers
from django.conf.urls import url, include
#from rest_framework import permissions

from .models.Cajaingreso import Cajaingreso
from .models.Citahistorial import Citahistorial
from .models.Citainscripcion import Citainscripcion
from .models.Cliente import Cliente
from .models.Cuentausuario import Cuentausuario
from .models.Especialidad import Especialidad
from .models.Odontologo import Odontologo
# Serializers define the API representation.


class CajaingresoSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    codigo_usu = serializers.ReadOnlyField(
        source='codigo_usuar.codigo_usuario')

    serie_ins = serializers.ReadOnlyField(
        source='serie_inscrip.serie')  # envia ID para CRUD

    serie_inss = serializers.ReadOnlyField(
        source='serie_in.serie')  # envia string para listar

    class Meta:
        model = Cajaingreso
        fields = ('url', 'id', 'codigo_usuar', 'codigo_usu',
                  'serie_inscrip', 'serie_ins',
                  'serie_in', 'serie_inss',
                  'dni_pagador', 'direccion', 'monto', 'fecha', 'estado_caja')


class CitahistorialSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    serie_ins = serializers.ReadOnlyField(
        source='serie_inscrip.serie')  # envia string para listar

    nombre_espe = serializers.ReadOnlyField(
        source='nombre_especiali.nombre_especialidad')  # envia string para listar

    class Meta:
        model = Citahistorial
        fields = ('url', 'id', 'serie_inscrip', 'serie_ins', 'nombre_especiali', 'nombre_espe', 'fecha_atencion',
                  'fecha_atender', 'descripcion', 'precio_un', 'cantidad')


class CitainscripcionSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    apellidos_cli = serializers.ReadOnlyField(
        source='apellidos_clien.apellidos_cliente')  # envia string para listar

    apellidos_odon = serializers.ReadOnlyField(
        source='apellidos_odonto.apellidos_odontologo')  # envia string para listar

    class Meta:
        model = Citainscripcion
        fields = ('url', 'id', 'apellidos_clien', 'apellidos_cli', 'apellidos_odonto', 'apellidos_odon', 'serie', 'ruc', 'tipo_pago',
                  'tipodocumento_pago', 'direccion', 'fecha_citasuscripcion', 'fecha_citaatender')


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente
        fields = ('url', 'id', 'apellidos_cliente', 'nombre_cliente', 'direccion_cliente', 'telefono_cliente',
                  'tipodoc_cliente', 'numdoc_cliente', 'email_cliente', 'genero_cliente', 'fechasuscripcion_cliente')


class CuentausuarioSerializer(serializers.ModelSerializer):
    # PARA MANDAR OTROS PARAMETROS DISTINTO AL ID
    apellidos_cli = serializers.ReadOnlyField(
        source='apellidos_clien.apellidos_cliente')  # envia string para listar

    class Meta:
        model = Cuentausuario
        fields = ('url', 'id', 'apellidos_clien', 'apellidos_cli', 'codigo_usuario', 'password',
                  'saldo', 'fechasuscripcion_usuario')


class EspecialidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Especialidad
        fields = ('url', 'id', 'nombre_especialidad',
                  'descripcion', 'precio_especialidad')


class OdontologoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Odontologo
        fields = ('url', 'id', 'apellidos_odontologo', 'nombre_odontologo', 'direccion_odontologo', 'telefono_odontologo',
                  'tipodoc_odontologo', 'numdoc_odontologo', 'email_odontologo', 'genero_odontologo')
