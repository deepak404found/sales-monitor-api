from django.db import models


class Product(models.Model):
    """
    Product model to store the product details

    Attributes:
        title: str: Name of the product
        price: float: Cost of the product
        description: str:  A brief description of the product
        category: str: category of the product
        image: str: URL for the product image
        sold: bool:  Boolean indicating whether the product is sold
        is_sale: bool: : Boolean indicating whether the product is on sale
        date_of_sale: date: Date of sale of the product

    """

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)
    image = models.URLField()
    sold = models.BooleanField(auto_created=True, default=False)
    is_sale = models.BooleanField(auto_created=True, default=False)
    date_of_sale = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"
