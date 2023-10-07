from django.db import models
from django.contrib.auth.models import User


class Instrutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    biografia = models.TextField()

    def __str__(self):
        return self.user.username


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    título = models.CharField(max_length=200)
    descrição = models.TextField()
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categoria, related_name="cursos")
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return self.título
