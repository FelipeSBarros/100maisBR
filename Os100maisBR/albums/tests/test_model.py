from django.test import TestCase

from Os100maisBR.albums.models import Album, Artista


class ArtistaModelTest(TestCase):
    def setUp(self):
        self.artista = Artista.objects.create(
            nome="Cartola",
            wikipedia_link="https://pt.wikipedia.org/wiki/Cartola_(compositor)",
        )

    def test_created(self):
        self.assertTrue(Artista.objects.exists())

    def test_wikpedia_can_be_blank(self):
        field = Artista._meta.get_field("wikipedia_link")
        self.assertTrue(field.blank)


class AlbumModelTest(TestCase):
    def setUp(self):
        self.album = Album.objects.create(
            titulo="Teste de album",
            ano=1989,
            wikipedia_link="https://pt.wikipedia.org/wiki/Cazuza",
        )
        self.album2 = Album.objects.create(
            titulo="Teste de album 2",
            ano=2010,
        )
        self.cartola = self.album.artista.create(
            nome="Cartola",
            wikipedia_link="https://pt.wikipedia.org/wiki/Cartola_(compositor)",
        )
        self.cazuza = self.album.artista.create(
            nome="cazuza",
            wikipedia_link="https://pt.wikipedia.org/wiki/Cazuza",
        )
        self.album.grades.create(grade=2)
        self.album.grades.create(grade=2)

    def test_created(self):
        self.assertTrue(Album.objects.exists())

    def test_album_has_artistas(self):
        self.assertEqual(2, self.album.artista.count())

    def test_album_has_many_grades(self):
        self.assertEqual(2, self.album.grades.count())

    def test_album_ordering(self):
        albums = Album.objects.all()
        albums = [album for album in albums]
        self.assertEquals(albums, [self.album2, self.album])
