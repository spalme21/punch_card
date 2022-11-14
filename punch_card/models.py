from django.db import models

class Client(models.Model):
    """A client"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    def __str__(self):
        """Return a string representation of the model."""
        return f'{self.last_name}, {self.first_name}'
        