from django.shortcuts import render

# Create your views here.
from ..models.Odontologo import Odontologo

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import OdontologoSerializer

# ViewSets define the view behavior.
class OdontologoViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Odontologo.objects.all()
    serializer_class = OdontologoSerializer
    