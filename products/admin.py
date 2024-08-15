from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from django.contrib import admin

from .models import Product, Category, ProductImage


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]


@admin.register(ProductImage)
class ProductAdmin(ModelAdmin):
    exclude = ["id", "status", "author"]


@admin.register(Category)
class ProductAdmin(ModelAdmin):
    pass


admin.site.unregister(Group)
