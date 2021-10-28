from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=16)

    def __str__(self):
        return self.title
