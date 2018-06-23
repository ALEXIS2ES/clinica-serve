from django.shortcuts import render

# Create your views here.
from ..models.Cliente import Cliente
from ..models.Cuentausuario import Cuentausuario

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import CuentausuarioSerializer

# ViewSets define the view behavior.


# API REST que permite a los usuarios ser vistos o editados.
class CuentausuarioViewSet(viewsets.ModelViewSet):
    queryset = Cuentausuario.objects.all()
    # queryset = Cuentausuario.objects.filter()
    serializer_class = CuentausuarioSerializer
