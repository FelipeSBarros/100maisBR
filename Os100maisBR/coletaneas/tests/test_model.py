from django.test import TestCase
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaModelTest(TestCase):
    def setUp(self):
        self.col1 = Coletanea(nome_coletanea="Felipe Barros", email="felipe@gmail.com")
        self.col1.save()

    def test_nome(self):
        assert self.col1.nome_coletanea == "Felipe Barros"

    # def test_slug(self):  # todo
    #     assert self.col1.slug == 'FelipeBarros'
