from django.db import models

"""
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
"""

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blogposts'

    def __str__(self) -> str:
        if len(self.title) < 50:
            return self.title
        else:
            return f"{self.title[:50]}.."
        