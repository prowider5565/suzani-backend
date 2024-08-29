from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "address",
            "sale_amount",
            "country",
            "phone_number",
            "region",
        ]
