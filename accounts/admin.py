from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    pass
