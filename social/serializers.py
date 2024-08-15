from rest_framework import serializers

from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["image", "url", "content_type"]

    # def to_representation(self, instance):
    #     context = super().to_representation(instance)
    #     for c in context:
    #         del c[c["content_type"]]

    #     return context


class SocialLinksSerializer(serializers.Serializer):
    facebook = serializers.URLField()
    twitter = serializers.URLField()
    instagram = serializers.URLField()
    watsup = serializers.URLField()
    telegram = serializers.URLField()

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context["author"] = instance.author
