from django.db import models
from imagekit import models as image_models
from imagekit import processors as image_proc
from django.contrib.auth.models import AbstractUser


class Autor(models.Model):
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="accounts/%Y/%m/%d", null=False, blank=True)

    foto_thumb = image_models.ImageSpecField(
        source="foto",
        processors=[image_proc.ResizeToFit(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )

    def __str__(self) -> str:
        return self.primeiro_nome


class Orientador(models.Model):
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    link_curriculo = models.URLField(max_length=500, unique=True)

    def __str__(self) -> str:
        return self.primeiro_nome


class Usuario(AbstractUser):
    pass
