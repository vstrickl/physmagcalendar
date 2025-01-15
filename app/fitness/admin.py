from django.contrib import admin

from .models import FitnessClass

# Register your models here.
class FitnessClassAdmin(admin.ModelAdmin):

    autocomplete_fields = ['class_name']

admin.site.register(FitnessClass, FitnessClassAdmin)
