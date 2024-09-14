from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.http import HttpRequest
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.urls import reverse
from typing import Any, List


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    exclude = ["id", "status", "author", "is_staff", "password", "groups"]
    readonly_fields = ["last_login", "date_joined"]

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        return list_display + ("delete_button",)

    def get_readonly_fields(self, request: HttpRequest, obj: Any = None) -> List[str]:
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and hasattr(obj, "role") and obj.role == "client":
            return readonly_fields + [field.name for field in obj._meta.fields]
        return readonly_fields

    def delete_button(self, obj):
        if obj.is_superuser:
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
        return request.user.is_superuser and request.user != obj
