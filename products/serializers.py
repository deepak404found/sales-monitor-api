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


class UpdateProductSerializers(serializers.ModelSerializer):
    """
    Serializer for updating a product
    """

    class Meta:
        model = Product
        fields = "__all__"


class SalesChartSerializer(serializers.Serializer):
    """
    Serializer for sales chart data
    """

    month = serializers.CharField()
    sales = serializers.DictField(
        child=serializers.DecimalField(max_digits=10, decimal_places=2)
    )


class ItemsChartSerializer(serializers.Serializer):
    """
    Serializer for items chart data
    """

    month = serializers.CharField()
    items = serializers.DictField(child=serializers.IntegerField())
