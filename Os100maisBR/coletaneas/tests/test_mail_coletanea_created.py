from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class ColetaneaNewPostValid(TestCase):
    def setUp(self):
        valida_data = dict(nome_coletanea="Coletanea da Vovó", email="user@host.com")
        self.resp = self.client.post(r("coletaneas:new"), valida_data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de criação nova coletânea'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = "felipe.b4rros@gmail.com"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['felipe.b4rros@gmail.com', 'user@host.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Coletanea da Vovó',
            'coletanea-da-vovo',
            ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
