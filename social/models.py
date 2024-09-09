from django.db import models

from accounts.models import BaseModel


class Advertisement(BaseModel):
    CHOICES = (("image", "Image"), ("video", "Video"))
    title = models.CharField(
        max_length=255, default="Defult title for an advertisement"
    )
    image = models.ImageField(upload_to="advertisements/", null=True)
    content_type = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.title


class SocialLinks(BaseModel):
    facebook = models.URLField(null=False, max_length=255)
    twitter = models.URLField(null=False, max_length=255)
    instagram = models.URLField(null=False, max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    watsup = models.URLField(null=False, max_length=255)
    telegram = models.URLField(null=False, max_length=255)

    def __str__(self):
        return f"Social Link: {self.email} - {self.phone_number}"
