from django.utils.html import format_html, mark_safe
from django.contrib.auth.models import Group
from django.forms.widgets import Media
from unfold.admin import ModelAdmin
from django.contrib import admin
from django.conf import settings

from .models import Product, Category, ProductImage
from accounts.mixins import DeleteButtonMixin


@admin.register(Product)
class ProductAdmin(DeleteButtonMixin, ModelAdmin):
    exclude = ["id", "status", "author"]
    list_display = ("display_image_name", "date_created")
    list_select_related = ("category",)

    def main_image(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if main_image:
            return format_html(
                '<img src="{}" style="border-radius: 50%; width: 50px; height: 50px; margin-right: 10px;" />',
                main_image.image.url,
            )
        # Return default image if no main image is found
        return format_html(
            '<img src="{}" style="border-radius: 50%; width: 50px; height: 50px; margin-right: 10px;" />',
            f"{settings.MEDIA_URL}default.png",
        )

    def display_image_name(self, obj):
        return format_html(
            '{} <strong>{}</strong> <span style="color: grey;">  {}</span>',
            self.main_image(obj),
            obj.name,
            (
                obj.description[:50] + "..."
                if len(obj.description) > 50
                else obj.description
            ),
        )

    display_image_name.short_description = "Product"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["clickable_rows"] = True

        response = super().changelist_view(request, extra_context=extra_context)

        # Inject the JavaScript directly into the template using mark_safe
        js_code = mark_safe(
            """
            <script>
                document.addEventListener('DOMContentLoaded', function() {
                    const rows = document.querySelectorAll('tr.change-row');
                    rows.forEach(function(row) {
                        row.addEventListener('click', function() {
                            const href = row.querySelector('a').getAttribute('href');
                            window.location.href = href;
                        });
                    });
                });
            </script>
            """
        )

        # Properly append the JavaScript to the media object
        response.context_data["media"] += Media(js=[js_code])

        return response


@admin.register(ProductImage)
class ProductImageAdmin(DeleteButtonMixin, ModelAdmin):
    exclude = ["id", "status", "author"]


@admin.register(Category)
class CategoryAdmin(DeleteButtonMixin, ModelAdmin):
    pass


admin.site.unregister(Group)
