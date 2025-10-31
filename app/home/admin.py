"""Admin view for DB Models"""
from django.contrib import admin
from django.utils.html import format_html

from .models import UploadFile, GymInfo

# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
    """Custom View for the Social Media Admin Panel."""
    search_fields = ('name',)
    list_display = ('name',)
admin.site.register(UploadFile, UploadFileAdmin)

class GymInfoAdmin(admin.ModelAdmin):
    """For Footer"""
    list_display = (
        "name",
        "copyright_year",
        "email",
        "feedback_form",
        "is_active",
        "logo"
    )

    def logo(self, obj):
        """Adds Thumbnail Image to FeedItems."""
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image)
        return "-"
    logo.short_description = 'Image'

admin.site.register(GymInfo, GymInfoAdmin)
