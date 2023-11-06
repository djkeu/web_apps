from django.db import models

class Pizza(models.Model):
    """Model a pizza."""
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Return a string presentation of the pizza."""
        return self.name
