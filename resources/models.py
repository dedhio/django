from django.db import models
from django.utils import timezone
from django.conf import settings


class ManagerControl(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=30)
    def __str__ (self):
        return self.name


class UseControl(models.Model):
    driver = models.ForeignKey('Driver', related_name='drivers')
    vehicle = models.ForeignKey('Vehicle', related_name='vehicles')
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.date_started

class Driver(models.Model):
    name = models.CharField(max_length=128)
    def __str__ (self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__ (self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=30)
    plate = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    licence_plate = models.CharField(max_length=7, blank=True)
    manufacture_year = models.DateField()
    is_active = models.BooleanField(default=True)
    creation_at = models.DateTimeField(auto_now=True) 
    update_at = models.DateTimeField(auto_now=True)

    manufacturer = models.ForeignKey('Manufacturer', related_name='my_vehicles')
    userControls = models.ManyToManyField(Driver, through='UseControl')
    def __str__ (self):
        return self.name