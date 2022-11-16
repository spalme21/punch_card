from django.test import TestCase


class IndexTest(TestCase):
    """Test index page"""

    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        