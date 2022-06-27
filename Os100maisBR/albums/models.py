from django.db import models


class Album(models.Model):
    titulo = models.CharField(verbose_name="Titulo do disco", max_length=255)
    ano = models.IntegerField(verbose_name="Ano de lançamento")
    artista = models.ManyToManyField("Artista", verbose_name="Artista(s)", blank=True)
    wikipedia_link = models.URLField(
        verbose_name="Link da wikipedia", blank=True, null=True
    )
    created_at = models.DateTimeField(
        verbose_name="Data e hora de criação", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Data e hora da última atualização", auto_now=True
    )
    grades = models.ManyToManyField("Grade")

    class Meta:
        verbose_name_plural = "Albums"
        verbose_name = "Album"
        ordering = ("-ano",)

    def __str__(self):
        return f"{self.titulo}, {self.ano}"


class Artista(models.Model):
    nome = models.CharField(verbose_name="Nome do(a) artista", max_length=255)
    wikipedia_link = models.URLField(
        verbose_name="Link da wikipedia", blank=True, null=True
    )
    created_at = models.DateTimeField(
        verbose_name="Data e hora de criação", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Data e hora da última atualização", auto_now=True
    )

    class Meta:
        verbose_name_plural = "Artistas"
        verbose_name = "Artista"
        ordering = ("nome",)

    def __str__(self):
        return self.nome


class Grade(models.Model):
    ONE_TO_FIVE = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    grade = models.IntegerField(
        verbose_name="Nota",
        help_text="Atribua uma nota a este album",
        choices=ONE_TO_FIVE,
        null=True,
    )  # todo como fazer o nullo pelo from (front)

    class Meta:
        verbose_name_plural = "Notas"
        verbose_name = "Nota"
