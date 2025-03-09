from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer

# import django_filters
from django_filters import FilterSet
import django_filters.rest_framework as django_filters


class ProductFilter(FilterSet):
    """
    Filter class for Product model to filter products.

    - min_price: Filter products with price greater than or equal to the given value.
    - max_price: Filter products with price less than or equal to the given value.
    - category: Filter products with the given category with case-insensitive match.
    - sold: Filter products with the given sold value (true or false).

    """

    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    category = django_filters.CharFilter(field_name="category", lookup_expr="iexact")

    class Meta:
        model = Product
        fields = {
            "sold": ["exact"],
        }


class ProductListView(generics.ListAPIView):
    """
    Product List View for listing and creating products.

    The view is inherited from ListCreateAPIView. The view is used to list all products and create a new product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    # filters
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        django_filters.DjangoFilterBackend,
    ]

    filterset_class = ProductFilter

    # search fields
    search_fields = ["title"]

    # ordering fields
    ordering_fields = ["price", "title"]
