from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import Advertisement, SocialLinks
from .forms import AdvertisementForm
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(ModelAdmin):
    form = AdvertisementForm
    exclude = ["id", "status", "author"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["image"].required = False
        form.base_fields["url"].required = False
        return form


@admin.register(SocialLinks)
class SocialLinkAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]
