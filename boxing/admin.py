from django.contrib import admin

from .models import BoxingClass

# Register your models here.
class BoxingClassAdmin(admin.ModelAdmin):

    autocomplete_fields = ['class_name']

admin.site.register(BoxingClass, BoxingClassAdmin)
