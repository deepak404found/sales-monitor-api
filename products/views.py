import django_filters.rest_framework as django_filters
from django.db.models import Count, Max, Min, Sum
from django.db.models.functions import TruncMonth

# import django_filters
from django_filters import FilterSet
from rest_framework import filters, generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import (
    ItemsChartSerializer,
    ProductSerializer,
    SalesChartSerializer,
)


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


class ProductCreateView(generics.CreateAPIView):
    """
    Product Create View for creating products.

    - use method POST to create a new product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateView(generics.UpdateAPIView):
    """
    Product Update View for updating products.

    - use method PUT to update a product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDeleteView(generics.DestroyAPIView):
    """
    Product Delete View for deleting products.

    - use method DELETE to delete a product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


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


class SalesChartView(APIView):
    """
    Sales Chart View

    This view generates and returns data for a chart showing the total sales in each category,
    grouped by month.

    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = (
            Product.objects.filter(sold=True)
            .annotate(month=TruncMonth("date_of_sale"))
            .values("month", "category")
            .annotate(total_sales=Sum("price"))
            .order_by("month")
        )

        # Create a dictionary to group by month
        grouped_data = {}
        for item in data:
            month = item["month"].strftime("%b %Y") if item["month"] else None
            category = item["category"]
            total_sales = item["total_sales"]

            if month not in grouped_data:
                grouped_data[month] = {"month": month, "sales": {}}

            grouped_data[month]["sales"][category] = total_sales

        # Ensure all categories are present even if zero sales
        all_categories = Product.objects.values_list("category", flat=True).distinct()
        for month in grouped_data:
            for category in all_categories:
                if category not in grouped_data[month]["sales"]:
                    grouped_data[month]["sales"][category] = 0

        # Convert to list
        result = list(grouped_data.values())

        serializer = SalesChartSerializer(result, many=True)
        return Response(serializer.data)


class ItemsChartView(APIView):
    """
    Items Chart View

    This view generates and returns data for a chart showing the total number of items sold
    in each category, grouped by month.
    """

    def get(self, request, *args, **kwargs):
        data = (
            Product.objects.filter(sold=True)
            .annotate(month=TruncMonth("date_of_sale"))
            .values("month", "category")
            .annotate(total_items=Count("id"))
            .order_by("month")
        )

        # Group the data by month and category
        grouped_data = {}
        for item in data:
            month = item["month"].strftime("%b %Y") if item["month"] else None
            category = item["category"]
            total_items = item["total_items"]

            if month not in grouped_data:
                grouped_data[month] = {"month": month, "items": {}}

            grouped_data[month]["items"][category] = total_items

        # Ensure all categories are present even if no items were sold
        all_categories = Product.objects.values_list("category", flat=True).distinct()
        for month in grouped_data:
            for category in all_categories:
                if category not in grouped_data[month]["items"]:
                    grouped_data[month]["items"][category] = 0

        # Convert to list
        result = list(grouped_data.values())

        # ✅ Use the serializer here:
        serializer = ItemsChartSerializer(result, many=True)
        return Response(serializer.data)
