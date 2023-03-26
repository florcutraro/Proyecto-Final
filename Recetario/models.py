from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    plato = models.CharField(max_length=100)
    resumen = models.TextField(max_length=1000)
    tiempo_en_min = models.IntegerField()
    porciones = models.IntegerField()
    ingredientes = models.TextField()
    pasos = models.TextField()
    fecha_de_carga = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="fotos", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="propietario")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''
    
    def __str__(self):
        return f"{self.id} - {self.plato}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''
    

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")

