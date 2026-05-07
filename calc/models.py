from django.db import models


class Example(models.Model):
    text = models.CharField(max_length=100)
    result = models.CharField(max_length=100)