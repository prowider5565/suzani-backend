from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters

from .pagination import ProductsPagination, ReviewPagination
from .models import Product, Review, ProductImage, Category
from .filters import ProductFilter, ReviewFilterSet
from .serializers import (
    ProductImageSerializer,
    ProductsSerializer,
    CategorySerializer,
    ReviewSerializer,
)


class ProductsListAPIView(ListAPIView):
    model = Product
    pagination_class = ProductsPagination
    serializer_class = ProductsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    queryset = Product.objects.all().order_by("date_created")
    search_fields = [
        "name",
        "description",
        "category__name",
        "price",
        "discount_price",
        "stock_quantity",
        "reviews__full_name",
        "reviews__comment",
        "reviews__rating",
    ]


class ProductsDetailAPIView(RetrieveAPIView):
    model = Product
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        product_images = ProductImage.objects.filter(product=instance)
        product_images_serializer = ProductImageSerializer(
            instance=product_images, many=True
        )
        images_list =[row["image"] for row in product_images_serializer.data]
        if not images_list:
            images_list.append("/media/default.png")
        data["images"] = images_list
        return Response(data)


class ReviewListCreateAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    model = Review
    queryset = Review.objects.all()
    pagination_class = ReviewPagination
    filterset_class = ReviewFilterSet


class CategoryListAPIView(ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
