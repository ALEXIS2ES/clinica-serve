from django.shortcuts import render

# Create your views here.
from ..models.Citainscripcion import Citainscripcion
from ..models.Especialidad import Especialidad
from ..models.Citahistorial import Citahistorial

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import CitahistorialSerializer

# ViewSets define the view behavior.
class CitahistorialViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Citahistorial.objects.all()
    serializer_class = CitahistorialSerializer
    