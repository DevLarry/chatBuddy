from django.test import SimpleTestCase
from django.urls import reverse, resolve


class UrlTests(SimpleTestCase):
    def home_url_resolves(self):
        assert 1 == 2