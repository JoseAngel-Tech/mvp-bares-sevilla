from django.db import models


class Bar(models.Model):

    # Información principal
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(
    unique=True,
    null=True,
    blank=True
)

    descripcion_corta = models.CharField(max_length=200)
    historia = models.TextField(blank=True)

    # Ubicación
    localidad = models.CharField(max_length=100, default="Sevilla")
    zona = models.CharField(max_length=100)
    subzona = models.CharField(max_length=100, blank=True)

    direccion = models.CharField(max_length=200)

    # Coordenadas (preparado para mapa futuro)
    latitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    # Clasificación
    categoria = models.CharField(max_length=100)

    caracteristicas = models.CharField(
        max_length=250,
        blank=True
    )

    # Información práctica
    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    horario = models.TextField(
        blank=True
    )

    # Multimedia
    imagen_url = models.URLField(
        blank=True
    )

    # Valoraciones
    valoracion_media = models.FloatField(default=0)

    numero_valoraciones = models.IntegerField(default=0)

    # Metadatos
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.nombre