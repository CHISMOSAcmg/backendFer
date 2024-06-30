from rest_framework import serializers
from .models import Queja, Sugerencia, Proceso, Subproceso

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = '__all__'

class SubprocesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subproceso
        fields = '__all__'

class QuejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queja
        fields = '__all__'

class SugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sugerencia
        fields = '__all__'
