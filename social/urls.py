from django.urls import path

from .views import add_social_media_links, get_social_links, AdvertisementAPIView


urlpatterns = [
    path("links/", add_social_media_links),
    path("links/list/", get_social_links),
    path("advertisements/", AdvertisementAPIView.as_view()),
]
