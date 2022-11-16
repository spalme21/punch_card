from django.test import TestCase

from punch_card.models import Client

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up sample client for testing"""
        Client.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="johndoe@email.com"
        )

    def test_first_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'First name')

    def test_first_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 30)

    def test_last_name_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Last name')

    def test_last_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('lirst_name').max_length
        self.assertEqual(max_length, 30)

    def test_phone_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'Phone')

    def test_phone_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('phone').max_length
        self.assertEqual(max_length, 15)

    def test_email_label(self):
        client = Client.objects.get(id=1)
        field_label = client._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Email')

    def test_email_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_object_name_is_last_name_comma_first_name(self):
        client = Client.objects.get(id=1)
        expected_object_name = f"{client.last_name}, {client.first_name}"
        self.assertEqual(str(client), expected_object_name)