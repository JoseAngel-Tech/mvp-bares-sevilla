from rest_framework import viewsets

from .models import Bar

from .serializers import (
    BarListSerializer,
    BarDetailSerializer,
)


class BarViewSet(viewsets.ModelViewSet):

    queryset = Bar.objects.all()


    def get_serializer_class(self):

        if self.action == 'list':
            return BarListSerializer

        return BarDetailSerializer


    filterset_fields = [
        'localidad',
        'zona',
        'categoria',
    ]


    search_fields = [
        'nombre',
        'descripcion',
        'historia',
        'especialidades',
    ]


    ordering_fields = [
        'valoracion_media',
        'numero_valoraciones',
        'fecha_actualizacion',
    ]