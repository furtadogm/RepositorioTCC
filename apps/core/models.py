from django.db import models
from imagekit import models as image_models
from imagekit import processors as image_proc
from .enums import MODALIDADE


class Autor(models.Model):

    primeiro_nome = models.CharField(max_length=255, verbose_name="Primeiro nome")
    ultimo_nome = models.CharField(max_length=255, verbose_name="Último nome")

    foto = models.ImageField(upload_to="accounts/%Y/%m/%d", null=False, blank=True)
    foto_miniatura = image_models.ImageSpecField(
        source="foto",
        processors=[image_proc.ResizeToFit(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )

    def __str__(self):
        return self.primeiro_nome


class Orientador(models.Model):
    primeiro_nome = models.CharField(max_length=255, verbose_name="Primeiro nome")
    ultimo_nome = models.CharField(max_length=255, verbose_name="Último nome")
    link_curriculo_lattes = models.URLField(
        max_length=255, verbose_name="Link do currículo lattes"
    )

    def __str__(self):
        return self.primeiro_nome


class Curso(models.Model):

    MODALIDADE_CHOICES = (
        (MODALIDADE.BACHARELADO, "Bacharelado"),
        (MODALIDADE.LICENCIATURA, "Licenciatura"),
        (MODALIDADE.TECNOLOGICO, "Tecnológico"),
    )

    nome = models.CharField(max_length=255, verbose_name="Nome")
    modalidade = models.IntegerField(choices=MODALIDADE_CHOICES)

    @property
    def get_modalidade(self):
        return self.MODALIDADE_CHOICES[self.modalidade][1]


class TCC(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    orientador = models.ForeignKey(
        Orientador, on_delete=models.SET_NULL, null=True, blank=True
    )
    ano_de_publicacao = models.DateField(verbose_name="Ano do documento")
    resumo = models.TextField(verbose_name="Resumo")
    arquivo = models.FileField(upload_to="tccs", verbose_name="Arquivo")
    palavras_chave = models.JSONField(default=list, verbose_name="Palavras chave")

    def __str__(self):
        return self.titulo
