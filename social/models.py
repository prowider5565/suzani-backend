from django.db import models

from accounts.models import BaseModel


class Advertisement(BaseModel):
    CHOICES = (("image", "Image"), ("video", "Video"))
    image = models.ImageField(upload_to="media/advertisements/", null=True)
    url = models.URLField(null=True, max_length=255)
    content_type = models.CharField(choices=CHOICES)
