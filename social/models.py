from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import BaseModel


class Advertisement(BaseModel):
    CHOICES = (("image", "Image"), ("video", "Video"))
    title = models.CharField(
        max_length=255, default="Defult title for an advertisement"
    )
    youtube_link = models.URLField(null=True, blank=True, default="")
    image = models.ImageField(upload_to="advertisements/", null=True, blank=True)
    content_type = models.CharField(choices=CHOICES)

    def clean(self):
        if not self.image and not self.youtube_link:
            raise ValidationError("Either an image or a YouTube link must be provided.")

    def save(self, *args, **kwargs):
        if self.image and self.youtube_link:
            # If both are provided, save two separate objects
            # First, save the video advertisement
            video_ad = Advertisement(
                title=self.title, youtube_link=self.youtube_link, content_type="video"
            )
            video_ad.save()

            # Then, update the current instance for the image and save it
            self.youtube_link = ""
            self.content_type = "image"
            super().save(*args, **kwargs)
        elif self.image:
            self.content_type = "image"
            super().save(*args, **kwargs)
        elif self.youtube_link:
            self.content_type = "video"
            super().save(*args, **kwargs)

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
