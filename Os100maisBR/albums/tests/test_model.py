from django.test import TestCase
from Os100maisBR.albums.models import Album, Artista
from django.shortcuts import resolve_url as r


class ArtistaModelTest(TestCase):
    def setUp(self):
        self.artista = Artista.objects.create(
            nome="Cartola",
            wikipedia_link="https://pt.wikipedia.org/wiki/Cartola_(compositor)",
        )

    def test_created(self):
        self.assertTrue(Artista.objects.exists())

    def test_description_can_be_blank(self):
        field = Artista._meta.get_field("wikipedia_link")
        self.assertTrue(field.blank)
