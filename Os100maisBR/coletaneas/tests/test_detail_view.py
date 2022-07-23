from django.shortcuts import resolve_url as r
from django.test import TestCase
from django.shortcuts import resolve_url as r
from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaDetailGet(TestCase):
    def setUp(self):
        Coletanea.objects.create(
            nome_coletanea="Coletanea da Vovó",
            email='user@host.com',
        )
        self.resp = self.client.get(r("coletaneas:detail", slug="coletanea-da-vovo"))

    def test_get(self):
        """ "GET should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "coletaneas/coletanea_detail.html")

    def test_html(self):
        contents = [
            "Obrigado por se inscrever!",
            "Coletanea da Vovó",
            "coletanea-da-vovo",
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """coletanea must be in context"""
        coletanea = self.resp.context["coletanea"]
        self.assertIsInstance(coletanea, Coletanea)


class ColetaneaDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r("coletaneas:detail", slug="not-found"))
        self.assertEqual(404, response.status_code)


class ColetaneaDetailView(TestCase):
    def setUp(self):
        self.resp = self.client.post(r("coletaneas:new"), {})


    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "coletaneas/coletanea_form.html")

    def test_has_form(self):
        form = self.resp.context["form"]
        self.assertIsInstance(form, ColetaneaForm)

    def test_form_has_errors(self):
        form = self.resp.context["form"]
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Coletanea.objects.exists())
