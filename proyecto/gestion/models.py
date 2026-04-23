from django.db import models

# Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.nombre


# Modelo Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def _str_(self):
        return self.titulo
