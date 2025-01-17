"""This module creates db models for the Boxing App."""
from django.db import models

from home.models import ClassType

# Create your models here.
class BoxingClass(models.Model):
    """Model for a boxing class."""
    class_name = models.ManyToManyField(ClassType, blank=True, related_name='boxing')
    day_time = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.class_name.name.exists():
            return f"{self.class_name.name}: {self.day_time}"
        return self.day_time
