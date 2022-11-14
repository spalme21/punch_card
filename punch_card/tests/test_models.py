from django.test import TestCase

from punch_card.models import Client

class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="johndoe@email.com"
        )
