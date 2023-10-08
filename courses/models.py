from django.db import models
from django.contrib.auth.models import User


class Instrutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    biografia = models.TextField()
    foto = models.ImageField(upload_to="img/instructors_pics/", default=None)

    def instrutor_foto_filename(instance, filename):
        ext = filename.split(".")[-1]
        return f"{instance.user.username}.{ext}"

    def save(self, *args, **kwargs):
        # Chama a função que define o caminho da imagem
        if self.foto:
            self.foto.name = self.instrutor_foto_filename(self.foto.name)
        super(Instrutor, self).save(*args, **kwargs)

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
    image = models.ImageField(upload_to="img/courses_pics/")
    data_envio = models.DateTimeField(auto_now=True)

    def curso_imagem_filename(instance, filename):
        ext = filename.split(".")[-1]
        return f"{instance.título}_{instance.instrutor}.{ext}"

    def save(self, *args, **kwargs):
        # Chama a função que define o caminho da imagem
        if self.image:
            self.image.name = self.curso_imagem_filename(self.image.name)
        super(Curso, self).save(*args, **kwargs)

    def __str__(self):
        return self.título


class Pedido(models.Model):
    AGUARDANDO_PAGAMENTO = "Aguardando Pagamento"
    CONCLUIDO = "Concluído"

    STATUS_CHOICES = [
        (AGUARDANDO_PAGAMENTO, "Aguardando Pagamento"),
        (CONCLUIDO, "Concluído"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=AGUARDANDO_PAGAMENTO
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)
