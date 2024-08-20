from django.db import models

from accounts.models import BaseModel


class Advertisement(BaseModel):
    CHOICES = (("image", "Image"), ("video", "Video"))
    image = models.ImageField(upload_to="media/advertisements/", null=True)
    url = models.URLField(null=True, max_length=255)
    content_type = models.CharField(choices=CHOICES)


class SocialLinks(BaseModel):
    facebook = models.URLField(null=False, max_length=255)
    twitter = models.URLField(null=False, max_length=255)
    instagram = models.URLField(null=False, max_length=255)
    watsup = models.URLField(null=False, max_length=255)
    telegram = models.URLField(null=False, max_length=255)

    def create(self, validated_data):
        self.objects.all().delete()
        return super().create(validated_data)


