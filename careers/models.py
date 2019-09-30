from django.db import models

# Create your models here.

class Career(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)