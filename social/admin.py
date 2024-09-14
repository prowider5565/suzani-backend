from django.utils.html import format_html
from unfold.admin import ModelAdmin
from django.conf import settings
from django.contrib import admin

from .models import Advertisement, SocialLinks
from accounts.mixins import DeleteButtonMixin
from .forms import AdvertisementForm
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(DeleteButtonMixin, ModelAdmin):
    form = AdvertisementForm
    exclude = ["id", "status", "author"]
    readonly_fields = ["content_type"]
    list_display = ("display_image_title",)


    def main_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="border-radius: 50%; width: 50px; height: 50px; margin-right: 10px;" />',
                obj.image.url,
            )
        return format_html(
            '<img src="{}" style="border-radius: 50%; width: 50px; height: 50px; margin-right: 10px;" />',
            f"{settings.MEDIA_URL}default.png",
        )

    def display_image_title(self, obj):
        return format_html(
            '{} <strong>{}</strong> <span style="color: grey;">',
            self.main_image(obj),
            obj.title,
        )


@admin.register(SocialLinks)
class SocialLinkAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
