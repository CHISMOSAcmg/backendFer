from rest_framework import viewsets
from .models import Queja, Sugerencia, Proceso, Subproceso
from .serializers import QuejaSerializer, SugerenciaSerializer, ProcesoSerializer, SubprocesoSerializer
from django.shortcuts import HttpResponse


class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer

class SubprocesoViewSet(viewsets.ModelViewSet):
    queryset = Subproceso.objects.all()
    serializer_class = SubprocesoSerializer

class QuejaViewSet(viewsets.ModelViewSet):
    queryset = Queja.objects.all()
    serializer_class = QuejaSerializer

class SugerenciaViewSet(viewsets.ModelViewSet):
    queryset = Sugerencia.objects.all()
    serializer_class = SugerenciaSerializer