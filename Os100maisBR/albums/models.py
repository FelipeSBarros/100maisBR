from django.db import models


class Album(models.Model):
    titulo = models.CharField(verbose_name="Titulo do disco", max_length=255)
    ano = models.IntegerField(verbose_name="Ano de lançamento")
    artista = models.ManyToManyField("Artista", verbose_name="Artista(s)")
    wikipedia_link = models.URLField(
        verbose_name="Link da wikipedia", blank=True, null=True
    )


class Artista(models.Model):
    nome = models.CharField(verbose_name="Nome do(a) artista", max_length=255)
    wikipedia_link = models.URLField(
        verbose_name="Link da wikipedia", blank=True, null=True
    )
