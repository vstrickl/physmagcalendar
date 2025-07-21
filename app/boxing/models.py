"""This module creates db models for the Boxing App."""
from django.db import models

from home.models import ClassType

# Create your models here.
class BoxingClass(models.Model):
    """Model for a boxing class."""
    class_name = models.ManyToManyField(ClassType, blank=True, related_name='boxing')
    day_time = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        class_names = ", ".join(c.name for c in self.class_name.all())  # pylint: disable=no-member
        day_time_str = str(self.day_time) if self.day_time else ""
        return f"{class_names}: {day_time_str}" if class_names else day_time_str
