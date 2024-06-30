from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcesoViewSet, SubprocesoViewSet, QuejaViewSet, SugerenciaViewSet

router = DefaultRouter()
router.register(r'procesos', ProcesoViewSet)
router.register(r'subprocesos', SubprocesoViewSet)
router.register(r'quejas', QuejaViewSet)
router.register(r'sugerencias', SugerenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
