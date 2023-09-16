import os
from http import HTTPStatus

import django
from django.test import TestCase
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path=path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['name_store'], "Coffee Like")


if __name__ == '__main__':
    h1 = IndexViewTestCase
    h1.test_view()
