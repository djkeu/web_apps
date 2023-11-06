from django.db import models

class Pizza(models.Model):
    """Model a pizza."""
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Return a string presentation of the pizza."""
        return self.name

class Topping(models.Model):
    """Model the toppings of a pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self) -> str:
        """Return a string represenation of the topping."""
        return f"{self.topping_name}"
