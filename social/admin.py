from unfold.admin import ModelAdmin
from django.contrib import admin


from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]
