from django.shortcuts import render

# Create your views here.
from ..models.Cliente import Cliente
from ..models.Odontologo import Odontologo
from ..models.Citainscripcion import Citainscripcion

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import CitainscripcionSerializer

# ViewSets define the view behavior.
class CitainscripcionViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Citainscripcion.objects.all()
    serializer_class = CitainscripcionSerializer
    