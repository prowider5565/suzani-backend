from rest_framework import serializers

from .models import Advertisement, SocialLinks


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ["image", "content_type"]


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"
