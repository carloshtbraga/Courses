# courses/signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import Curso


@receiver(pre_delete, sender=Curso)
def curso_pre_delete(sender, instance, **kwargs):
    # Obtenha o caminho da imagem associada ao curso
    image_path = instance.image.path

    # Exclua a imagem
    if default_storage.exists(image_path):
        default_storage.delete(image_path)
