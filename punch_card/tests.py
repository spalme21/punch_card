from django.urls import resolve
from django.test import TestCase
from punch_card.views import index

class IndexTest(TestCase):
    """Test index page"""

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
