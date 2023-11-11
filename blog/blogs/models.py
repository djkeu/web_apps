from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_addes = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
    