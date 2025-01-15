from django.contrib import admin

from .models import LiftingClass

# Register your models here.
class LiftingClassAdmin(admin.ModelAdmin):

    autocomplete_fields = ['class_name']

admin.site.register(LiftingClass, LiftingClassAdmin)
