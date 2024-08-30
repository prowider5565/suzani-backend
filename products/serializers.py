from rest_framework import serializers

from .models import Product, Category, ProductImage, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "id"]


class ProductsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"

        fields = [
            "name",
            "description",
            "price",
            "category",
            "discount_price",
            "stock_quantity",
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["uuid"] = instance.id

        image_object = ProductImage.objects.filter(is_main=True, product=instance)
        if image_object.exists():
            context["cover_image"] = "/media/" + str(image_object.first().image)
        else:
            context["cover_image"] = "/media/default.png"

        return context


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = ["id", "product", "full_name", "rating", "comment", "date_created"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["date_created"] = instance.date_created
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"
