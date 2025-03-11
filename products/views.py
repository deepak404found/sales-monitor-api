import django_filters.rest_framework as django_filters

# import django_filters
from django_filters import FilterSet
from rest_framework import filters, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Min, Max

from products.models import Product
from products.serializers import ProductSerializer


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
    # permission_classes = [IsAuthenticated]

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


class CategoriesListView(generics.ListAPIView):
    """
    Categories List View for listing all categories.

    The view is inherited from ListAPIView. The view is used to list all categories.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = Product.objects.values_list("category", flat=True).distinct()
        return Response(categories)


class PriceRangeView(APIView):
    """
    Price Range View for getting the price range of products.

    The view is inherited from ListAPIView. The view is used to get the price range of products.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        min_price = Product.objects.aggregate(min_price=Min("price"))["min_price"]
        max_price = Product.objects.aggregate(max_price=Max("price"))["max_price"]
        return Response({"min_price": min_price, "max_price": max_price})
