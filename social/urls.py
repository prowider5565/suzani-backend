from django.urls import path

from .views import SocialLinksListAPIView, AdvertisementAPIView


urlpatterns = [
    path("links/", SocialLinksListAPIView.as_view()),
    path("advertisements/", AdvertisementAPIView.as_view()),
]
