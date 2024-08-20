from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        content_type = cleaned_data.get("content_type")

        if content_type == "image" and not cleaned_data.get("image"):
            self.add_error("image", 'Image is required when content type is "Image".')

        if content_type == "video" and not cleaned_data.get("url"):
            self.add_error("url", 'URL is required when content type is "Video".')

        return cleaned_data
