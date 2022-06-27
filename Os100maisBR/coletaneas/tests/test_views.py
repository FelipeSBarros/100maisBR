from django.test import TestCase
from Os100maisBR.coletaneas.views import CreateColetanea
from django.shortcuts import resolve_url as r


class CreateColetaneaTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r("coletaneas:new"))

    def test_get(self):
        """GET /plot_create must get status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_use_template(self):
        """GET /new/ must use coletanea_form.html template"""
        self.assertTemplateUsed(self.resp, "coletaneas/coletanea_form.html")

    # todo test detail template
    # todo test not fund
    # def test_not_found(self):
    #     self.assertEqual(404, self.resp.status_code)
