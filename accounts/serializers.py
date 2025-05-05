from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "role"]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["id"] = instance.pk
        context["first_name"] = instance.first_name
        context["last_name"] = instance.last_name
        context["is_superuser"] = instance.is_superuser
        context["is_staff"] = instance.is_staff
        context["date_joined"] = instance.date_joined
        context.pop("password")
        return context


class OTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=7)
