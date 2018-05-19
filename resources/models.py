from django.db import models
from django.utils import timezone
from django.conf import settings


class ManagerControl(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=30)


class UseControl(models.Model):
    driver = models.ForeignKey('Driver')
    vehicle = models.ForeignKey('Vehicle')
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(auto_now_add=True)


class Driver(models.Model):
    name = models.CharField(max_length=128)



class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__ (self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=30)
    plate = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    licence_plate = models.CharField(max_length=7, blank=True)
    manufacture_year = models.DateField()
    is_active = models.BooleanField(default=True)
    creation_at = models.DateTimeField(auto_now=True) 
    update_at = models.DateTimeField(auto_now=True)

    manufacturer = models.ForeignKey('Manufacturer')
    userControls = models.ManyToManyField(Driver, through='UseControl')