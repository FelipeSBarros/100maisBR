from django.shortcuts import resolve_url as r
from django.test import TestCase

from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r("coletaneas:new"))

    def test_get(self):
        """GET /plot_create must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_use_template(self):
        """GET /new/ must use coletanea_form.html template"""
        self.assertTemplateUsed(self.resp, "coletaneas/coletanea_form.html")

    def teste_html(self):
        """html must contain input tags"""
        tags = (  # todo revisar esses valores depois de excluir fields do forms
            ("<form", 2),
            ("<input", 4),
            ('type="text"', 2),
            ('type="email"', 1),
            ('type="submit"', 2),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """html must contains CSRF"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """context must have ColetaneaModelForm form"""
        form = self.resp.context["form"]
        self.assertIsInstance(form, ColetaneaForm)


class ColetaneaNewPostValid(TestCase):
    def setUp(self):
        valida_data = dict(nome_coletanea="Coletanea da Vovó", email="user@host.com")
        self.resp = self.client.post(r("coletaneas:new"), valida_data)

    def test_post(self):
        """Valid post should redirect to coletaneas/slug/"""
        self.assertRedirects(self.resp, r("coletaneas:detail", "coletanea-da-vovo"))

    # todo test_send_subscribe_email

    def test_save_coletanea(self):
        self.assertTrue(Coletanea.objects.exists())


class ColetaneaNewPostInvalid(TestCase):
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
