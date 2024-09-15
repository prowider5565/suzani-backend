from django.urls import reverse
from django.utils.html import format_html


class DeleteButtonMixin:
    def delete_button(self, obj):
        return format_html(
            '<div style="text-align: right;">'
            '<a href="{}" style="color: #d9534f; border: 2px solid #d9534f; padding: 6px 12px; border-radius: 5px; text-decoration: none; background-color: transparent; transition: background-color 0.3s, color 0.3s;">'
            "🗑️ Delete</a></div>",
            reverse(
                f"admin:{obj._meta.app_label}_{obj._meta.model_name}_delete",
                args=[obj.pk],
            ),
        )

    delete_button.short_description = "Delete"

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        return list_display + ("delete_button",)
