from django.shortcuts import render

# Create your views here.
from ..models.Especialidad import Especialidad

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import EspecialidadSerializer

# ViewSets define the view behavior.
class EspecialidadViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    