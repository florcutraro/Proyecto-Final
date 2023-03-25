from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    plato = models.CharField(max_length=100)
    resumen = models.TextField(max_length=1000)
    tiempo_en_min = models.IntegerField()
    porciones = models.FloatField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    fecha_de_carga = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="menues", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="propietario")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''
    
    def __str__(self):
        return f"{self.id} - {self.plato} - {self.propietario.id}"


