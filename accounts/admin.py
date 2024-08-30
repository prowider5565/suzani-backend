from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.http import HttpRequest
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.urls import reverse
from typing import Any


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]

    def get_readonly_fields(self, request, obj=None):
        if obj and obj == request.user:
            # Make all fields readonly for the current user
            return [field.name for field in obj._meta.fields]
        return super().get_readonly_fields(request, obj)

    def delete_button(self, obj):
        if obj == self.request.user:
            # If the current object is the logged-in user, show a disabled delete button
            return format_html(
                '<div style="text-align: right;">'
                '<a class="button" style="color: white; background-color: #6c757d; padding: 6px 12px; border-radius: 5px; text-decoration: none; pointer-events: none; cursor: not-allowed;">'
                "🚫 Delete Disabled</a></div>"
            )
        else:
            # Otherwise, show the normal delete button
            return format_html(
                '<div style="text-align: right;">'
                '<a href="{}" class="button" style="color: white; background-color: #d9534f; padding: 6px 12px; border-radius: 5px; text-decoration: none;">'
                "🗑️ Delete</a></div>",
                reverse(
                    f"admin:{obj._meta.app_label}_{obj._meta.model_name}_delete",
                    args=[obj.pk],
                ),
            )

    delete_button.short_description = "Delete"

    def has_delete_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return obj == request.user
