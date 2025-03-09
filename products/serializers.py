# from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id"]
