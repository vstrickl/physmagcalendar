"""The module creates base models for the calendar app."""
from django.db import models

# Create your models here.
class ClassType (models.Model):
    """Defines class types"""
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class GymInfo(models.Model):
    """Defines gym information"""
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    copyright_year = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    gym_logo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
