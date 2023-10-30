from django.db import models

from home.models import ClassType

# Create your models here.
class FitnessClass(models.Model):
    class_name = models.ManyToManyField(ClassType, blank=True, related_name='fitness')
    day_time = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.class_name.exists():
            return f"{self.class_name.first().name}: {self.day_time}"
        else:
            return self.day_time
