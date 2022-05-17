from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self) -> None:
        """Create response instance atribute used on tests"""
        self.response = self.client.get(r("core:home"))

    def test_get(self):
        """GET must return HTTP status 200"""
        self.assertAlmostEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        expected = f"href={r('core:home')}"
