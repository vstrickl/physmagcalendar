from django.contrib import admin

from .models import StudioClass

# Register your models here.
class StudioClassAdmin(admin.ModelAdmin):

    autocomplete_fields = ['class_name']

admin.site.register(StudioClass, StudioClassAdmin)