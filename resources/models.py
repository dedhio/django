from django.db import models

# Create your models here.
class Vehicle(models.Model):

    name = models.CharField(max_length=30)
    plate = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)