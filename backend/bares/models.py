from django.db import models

class Bar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    zona = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre