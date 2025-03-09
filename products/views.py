from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    """
    Product List View for listing and creating products.

    The view is inherited from ListCreateAPIView. The view is used to list all products and create a new product.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
