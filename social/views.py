from rest_framework.generics import ListAPIView

from .serializers import AdvertisementSerializer, SocialLinksSerializer
from .models import Advertisement, SocialLinks


class AdvertisementAPIView(ListAPIView):
    model = Advertisement
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # permission_classes = [IsManager]


# @api_view(["POST"])
# @permission_classes([IsManager])
# def add_social_media_links(request):
#     social_link_serializer = SocialLinksSerializer(request.data)
#     social_link_serializer.is_valid(raise_exception=True)
#     social_link_serializer["author"] = request.user
#     connection = get_redis_connection()
#     connection.delete("social_links")
#     connection.set("social_links", json.dumps(social_link_serializer.validated_data))
#     return Response(json.loads(connection.get("social_links")))


# @api_view(["GET"])
# def get_social_links(request):
#     connection = get_redis_connection()
#     social_links = connection.get("social_links")
#     if social_links is None:
#         return Response({"msg": "No social media links found!"}, status=404)
#     social_links_serializer = SocialLinksSerializer(
#         data=json.loads(connection.get("social_links"))
#     )
#     return Response(social_links_serializer.validated_data)


class SocialLinksListAPIView(ListAPIView):
    serializer_class = SocialLinksSerializer
    queryset = SocialLinks.objects.all()

    def get_queryset(self):
        queryset = self.queryset.order_by("-date_created").last()
        return [queryset]
