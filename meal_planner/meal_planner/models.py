from django.db import models

class Meal(models.Model):
    """Model a meal."""
    text = models.CharField(max_length=20)

    def __str__(self) -> str:
        """Return string representation of a meal."""
        return self.text
    