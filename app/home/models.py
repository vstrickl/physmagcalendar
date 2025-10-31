"""The module creates base models for the calendar app."""
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class UploadFile(models.Model):
    """Model for uploaded files."""
    name = models.CharField(max_length=255)
    image = CloudinaryField(
        'image',
        folder="uploads/",
        allowed_formats=["jpg", "png", "jpeg"],
        transformation={"quality": "auto"},
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

class GymInfo(models.Model):
    """Defines gym information"""
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    copyright_year = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=1000, null=True, blank=True)
    logo = CloudinaryField(
        'image',
        folder="uploads/",
        allowed_formats=["jpg", "png", "jpeg"],
        transformation={"quality": "auto"},
        blank=True, null=True
    )
    feedback_form = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
