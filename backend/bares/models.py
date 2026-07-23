from django.db import models


class Bar(models.Model):

    nombre = models.CharField(max_length=100)

    slug = models.SlugField(
    unique=True,
    blank=True,
    null=True
)


    descripcion = models.TextField(
        blank=True
    )

    historia = models.TextField(
        blank=True
    )


    localidad = models.CharField(
        max_length=100
    )

    zona = models.CharField(
        max_length=100
    )

    subzona = models.CharField(
        max_length=100,
        blank=True
    )


    direccion = models.CharField(
        max_length=200
    )


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


    categoria = models.CharField(
        max_length=100
    )


    caracteristicas = models.TextField(
        blank=True
    )

    especialidades = models.TextField(
        blank=True
    )


    ambiente = models.CharField(
        max_length=100,
        blank=True
    )

    ideal_para = models.CharField(
        max_length=200,
        blank=True
    )

    precio_medio = models.CharField(
        max_length=50,
        blank=True
    )


    telefono = models.CharField(
        max_length=20,
        blank=True
    )


    horario = models.TextField(
        blank=True
    )


    imagen_url = models.URLField(
        blank=True
    )


    valoracion_media = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0
    )


    numero_valoraciones = models.IntegerField(
        default=0
    )


    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.nombre