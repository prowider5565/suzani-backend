from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]
    readonly_fields = [
        "full_name",
        "address",
        "country",
        "region",
        "sale_amount",
        "phone_number",
    ]

    def has_add_permission(self, request):
        return False
