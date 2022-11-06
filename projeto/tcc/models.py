from django.db import models
from usuario.models import Autor, Orientador
import os
from django.core.exceptions import ValidationError


class Curso(models.Model):
    MODALIDADE_ESCOLHAS = [
        (0, "Bacharelado"),
        (1, "Licenciatura"),
        (2, "Tecnológico"),
    ]
    nome = models.CharField(max_length=255)
    modalidade = models.IntegerField(choices=MODALIDADE_ESCOLHAS)

    def __str__(self) -> str:
        return self.nome


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".pdf"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Apenas documentos .pdf")


class TCC(models.Model):
    arquivo = models.FileField(
        upload_to="arquivos/%Y/%m/%d/", validators=[validate_file_extension]
    )
    resumo = models.TextField()
    titulo = models.CharField(max_length=250)
    ano_doc = models.IntegerField()
    palavra_chave = models.JSONField(default=list)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo
