from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoría")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoría")

    def __str__(self):
        return self.nombreCategoria
    
class Planta(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8, verbose_name="Codigo")
    tipo = models.CharField(max_length=50, blank=True, verbose_name="Tipo")
    ambiente = models.CharField(max_length=50, blank=True, verbose_name="Ambiente")
    garantia = models.CharField(max_length=50, blank=True, verbose_name="Garantia")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.codigo