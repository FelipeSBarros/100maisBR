from django.test import TestCase

from Os100maisBR.coletaneas.forms import ColetaneaForm


class ColetaneaFormTest(TestCase):
    def test_form_has_fields(self):
        """form must have 2 fields"""
        form = ColetaneaForm()
        expected = ["nome_coletanea", "email"]
        self.assertSequenceEqual(expected, list(form.fields))

    def assertFormCode(self, form, field, code):
        error = form.errors.as_data()
        error_list = error[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]

        self.assertListEqual([msg], errors_list)
