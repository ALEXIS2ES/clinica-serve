from django.shortcuts import render

# Create your views here.
from ..models.Cuentausuario import Cuentausuario
from ..models.Citainscripcion import Citainscripcion
from ..models.Cajaingreso import Cajaingreso

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from ..serializers import CajaingresoSerializer

# ViewSets define the view behavior.
class CajaingresoViewSet(viewsets.ModelViewSet):  # API REST que permite a los usuarios ser vistos o editados.
    queryset = Cajaingreso.objects.all()
    serializer_class = CajaingresoSerializer
    #queryset = Cajaingreso.objects.filter()

    #def get_queryset(self):
        #query = self.request.query_params.get('query', '')
        #queryall = (Q(direccion__icontains=query),
                    #Q(monto__icontains=query),
                    #Q(fecha__icontains=query),
                    #Q(estado_caja__icontains=query))
        #queryset = self.queryset.filter(reduce(OR, queryall))
        #return queryset