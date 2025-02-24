from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
CATEGORIAS = (
    ('1', 'Violencia'),
    ('2', 'Robo'),
    ('3', 'Otros'),
)

class Denuncia(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(default='pendiente', max_length=20)
    categoria = models.CharField(choices=CATEGORIAS, max_length=20)
    imagen = models.ImageField(upload_to='images/')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

admin.site.register(Denuncia)