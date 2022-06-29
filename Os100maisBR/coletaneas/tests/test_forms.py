# from django.test import TestCase
#
# from Os100maisBR.coletaneas.forms import ColetaneaForm
#
#
# class ColetaneaFormTest(TestCase):
#     def test_form_has_fields(self):
#         """form must have 2 fields"""
#         form = ColetaneaForm()
#         expected = ["nome_coletanea", "email"]
#         self.assertSequenceEqual(expected, list(form.fields))
#
#     # def test_cpf_is_digit(self):
#     #     """CPF must only accept digits."""
#     #     form = self.make_validated_form(cpf="ABCD5678901")
#     #     self.assertFormCode(form, "cpf", "digits")
#     #
#     # def test_cpf_has_11_digits(self):
#     #     """CPF field must have 11 digits"""
#     #     form = self.make_validated_form(cpf="1234")
#     #     self.assertFormCode(form, "cpf", "length")
#     #
#     # def assertFormCode(self, form, field, code):
#     #     error = form.errors.as_data()
#     #     error_list = error[field]
#     #     exception = error_list[0]
#     #     self.assertEqual(code, exception.code)
#     #
#     # def assertFormErrorMessage(self, form, field, msg):
#     #     errors = form.errors
#     #     errors_list = errors[field]
#     #
#     #     self.assertListEqual([msg], errors_list)
#     #
#     # def make_validated_form(self, **kwargs):
#     #     valid = dict(
#     #         name="Felipe", cpf="12345678901", email="fe@sd.com", phone="21-996186180"
#     #     )
#     #     data = dict(valid, **kwargs)
#     #     form = SubscriptionForm(data)
#     #     form.is_valid()
#     #     return form
#     #
#     # def test_name_must_bu_capitalized(self):
#     #     """Name must bu copitilized."""
#     #     # HENRIQUE BASTOS -> Henrique Bastos
#     #     form = self.make_validated_form(name="HENRIQUE Bastos")
#     #     self.assertEqual("Henrique Bastos", form.cleaned_data["name"])
#     #
#     # def test_email_is_optional(self):
#     #     """email is optional"""
#     #     form = self.make_validated_form(email="")
#     #     self.assertFalse(form.errors)
#     #
#     # def test_phone_is_optional(self):
#     #     """phone is optional"""
#     #     form = self.make_validated_form(phone="")
#     #     self.assertFalse(form.errors)
#     #
#     # def test_must_inform_email_or_phone(self):
#     #     """Email and phone are optional, but one must be informed"""
#     #     form = self.make_validated_form(phone="", email="")
#     #     self.assertListEqual(["__all__"], list(form.errors))
