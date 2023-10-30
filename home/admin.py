from django.contrib import admin

from .models import ClassType, GymInfo

# Register your models here.
class ClassTypeAdmin(admin.ModelAdmin):

    search_fields = ['name']

admin.site.register(ClassType, ClassTypeAdmin)

class GymInfoAdmin(admin.ModelAdmin):

    list_display = ("name", "copyright_year", "email")

admin.site.register(GymInfo, GymInfoAdmin)