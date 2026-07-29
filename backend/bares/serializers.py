from rest_framework import serializers

from .models import Bar


class BarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bar

        fields = [
            'id',
            'nombre',
            'localidad',
            'zona',
            'categoria',
            'imagen_url',
            'valoracion_media',
            'numero_valoraciones',
        ]


class BarDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bar

        fields = '__all__'


    def validate_valoracion_media(self, value):

        if value < 0 or value > 5:
            raise serializers.ValidationError(
                "La valoración debe estar entre 0 y 5."
            )

        return value


    def validate_numero_valoraciones(self, value):

        if value < 0:
            raise serializers.ValidationError(
                "El número de valoraciones no puede ser negativo."
            )

        return value
