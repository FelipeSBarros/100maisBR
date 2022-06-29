from django.test import TestCase

from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaModelTest(TestCase):
    def setUp(self):
        self.col1 = Coletanea.objects.create(
            nome_coletanea="Coletanea da Vovozinha", email="vovozinha@gmail.com"
        )

    def test_nome(self):
        assert self.col1.nome_coletanea == "Coletanea da Vovozinha"

    def test_slug_is_created_automatcally(self):
        assert self.col1.slug == "coletanea-da-vovozinha"
