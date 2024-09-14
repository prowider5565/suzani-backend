from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            content_type = self.instance.content_type
            if content_type == "video":
                self.fields["image"].widget = forms.HiddenInput()
            elif content_type == "image":
                self.fields["youtube_link"].widget = forms.HiddenInput()
