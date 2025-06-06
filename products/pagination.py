from rest_framework.pagination import PageNumberPagination


class ProductsPagination(PageNumberPagination):
    page_size = 16


class ReviewPagination(PageNumberPagination):
    page_size = 36
