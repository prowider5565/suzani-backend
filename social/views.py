from rest_framework.generics import ListAPIView

from .serializers import AdvertisementSerializer, SocialLinksSerializer
from .models import Advertisement, SocialLinks


class AdvertisementAPIView(ListAPIView):
    model = Advertisement
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class SocialLinksListAPIView(ListAPIView):
    serializer_class = SocialLinksSerializer
    queryset = SocialLinks.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by("-date_created").last()
        return [queryset]
