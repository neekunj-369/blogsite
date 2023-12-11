from django.db import models


class posts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000000000000000000000)

    def __str__(self):
        return self.title
# Create your models here.
