from django.db import models

class Bar(models.Model):
    # Información principal
    nombre = models.CharField(max_length=120)
    descripcion_corta = models.CharField(max_length=200)
    historia = models.TextField(blank=True)

    # Ubicación
    zona = models.CharField(max_length=100)
    subzona = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    # Clasificación
    categoria = models.CharField(max_length=100)

    # Información práctica
    telefono = models.CharField(max_length=20, blank=True)
    horario_apertura = models.CharField(max_length=50, blank=True)
    horario_cierre = models.CharField(max_length=50, blank=True)

    # Multimedia
    imagen = models.URLField(blank=True)

    # Valoración
    valoracion_media = models.FloatField(default=0)

    # Metadatos
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre