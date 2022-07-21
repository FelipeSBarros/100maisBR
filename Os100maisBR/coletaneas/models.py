from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Coletanea(models.Model):
    nome_coletanea = models.CharField(
        max_length=25, help_text="Defina um nome para a sua coletânea de discos."
    )
    email = models.EmailField(
        help_text="Usaremos o seu email apenas para enviar o link da sua coletânea por email."
    )
    albums = models.ManyToManyField("albums.Album", verbose_name="Albums", blank=True)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(
        verbose_name="Data e hora de criação", auto_now_add=True
    )
    last_visit = models.DateTimeField(
        verbose_name="Data e hora da última visita", auto_now=True
    )

    class Meta:
        verbose_name_plural = "Coletâneas"
        verbose_name = "Coletânea"

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse(
            "coletaneas:detail", kwargs={"slug": self.slug}
        )  # todo slug=self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome_coletanea)
        super(Coletanea, self).save(*args, **kwargs)
