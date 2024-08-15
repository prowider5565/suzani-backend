import django_filters
from .models import Product, Category, Tag, Review


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    rating = django_filters.NumericRangeFilter(
        field_name="reviews__rating", lookup_expr="range"
    )

    class Meta:
        model = Product
        fields = {"name": ["icontains"], "category": ["exact"]}
