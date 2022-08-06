from datetime import datetime, timezone, timedelta
from unittest import mock

from django.shortcuts import resolve_url as r
from django.test import TestCase

from Os100maisBR.coletaneas.forms import ColetaneaForm
from Os100maisBR.coletaneas.models import Coletanea


class ColetaneaDetailGet(TestCase):
    def setUp(self):
        Coletanea.objects.create(
            nome_coletanea="Coletanea da Vovó",
            email="user@host.com",
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


class ColetaneaLastVisitIsUpdated(TestCase):  # todo add message informando que publicação foi pausada
    def setUp(self):
        self.BR_TIME_ZONE = timezone(timedelta(hours=-3))
        self.mocked_date = datetime(2022, 1, 1, 0, 0, 0, tzinfo=self.BR_TIME_ZONE)
        with mock.patch(
            "django.utils.timezone.now", mock.Mock(return_value=self.mocked_date)
        ):
            self.col1 = Coletanea.objects.create(
                nome_coletanea="Coletanea da Vovozinha", email="vovozinha@gmail.com"
            )

    def test_last_visit_field_date(self):
        self.assertEqual(self.col1.last_visit, self.mocked_date)

    def test_get_method_update_last_visit_field(self):
        """ "GET should update last_visit model field"""
        self.resp = self.client.get(
            r("coletaneas:detail", slug="coletanea-da-vovozinha")
        )
        mocked_date2 = datetime(2022, 1, 3, 0, 0, 0, tzinfo=self.BR_TIME_ZONE)
        with mock.patch(
            "django.utils.timezone.now", mock.Mock(return_value=mocked_date2)
        ):
            self.resp = self.client.get(
                r("coletaneas:detail", slug="coletanea-da-vovozinha")
            )

        self.assertNotEqual(
            self.resp.context["coletanea"].last_visit.astimezone(self.BR_TIME_ZONE),
            self.mocked_date,
        )
        self.assertEqual(
            self.resp.context["coletanea"].last_visit.astimezone(self.BR_TIME_ZONE),
            mocked_date2,
        )


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
