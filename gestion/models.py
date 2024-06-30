from django.db import models
from django.contrib.auth.models import User

class Proceso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Subproceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Queja(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    proceso = models.ManyToManyField(Proceso)
    subproceso = models.ManyToManyField(Subproceso)
    estado = models.CharField(max_length=50)

class Sugerencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    proceso = models.ManyToManyField(Proceso)
    subproceso = models.ManyToManyField(Subproceso)
