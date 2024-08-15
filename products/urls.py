from django.urls import path

from .views import (
    ReviewListCreateAPIView,
    ProductsDetailAPIView,
    ProductsListAPIView,
    CategoryListAPIView,
)

urlpatterns = [
    path("list/", ProductsListAPIView.as_view()),
    path("detail/<uuid:id>/", ProductsDetailAPIView.as_view()),
    path("reviews/", ReviewListCreateAPIView.as_view()),
    path("categories/", CategoryListAPIView.as_view(), name="Category"),
]
