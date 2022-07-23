from django.test import TestCase

from Os100maisBR.albums.models import Album
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaModelTest(TestCase):
    def setUp(self):
        self.col1 = Coletanea.objects.create(
            nome_coletanea="Coletanea da Vovozinha", email="vovozinha@gmail.com"
        )
        self.album = Album.objects.create(
            titulo="Teste de album",
            ano=1989,
            wikipedia_link="https://pt.wikipedia.org/wiki/Cazuza",
        )
        self.album2 = Album.objects.create(
            titulo="Teste de album 2",
            ano=2010,
        )
        self.col1.albums.add(self.album)
        self.col1.albums.add(self.album2)

    def test_nome(self):
        assert self.col1.nome_coletanea == "Coletanea da Vovozinha"

    def test_slug_is_created_automatcally(self):
        assert self.col1.slug == "coletanea-da-vovozinha"

    def test_coletanea_has_published_albums(self):
        albums_publicados = [album for album in self.col1.albums.all()]
        self.assertEquals(albums_publicados, [self.album2, self.album])

# todo test if coletanea can vote on published Album
