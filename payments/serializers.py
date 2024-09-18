from rest_framework import serializers

from .models import Order, OrderSet


class OrderSetSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField(source="product.id")

    class Meta:
        model = OrderSet
        fields = ["product_id", "product_name", "count"]


class OrderSerializer(serializers.ModelSerializer):
    orders = OrderSetSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "full_name",
            "address",
            "sale_amount",
            "country",
            "phone_number",
            "region",
            "orders",
        ]
        