import json
from products.serializers import ProductSerializer
from products.models import Product  # Import the Product model


def run():
    print("Adding sample data...")

    # read the file .sampleData.json
    with open("products/scripts/sampleData.json", "r") as file:
        data = json.load(file)

    # loop through the data and create or update a product for each item
    for product in data:
        try:
            print("Processing product: ", product["title"])
            existing_product = Product.objects.filter(title=product["title"]).first()
            if existing_product:
                serializer = ProductSerializer(existing_product, data=product)
                action = "Updating"
            else:
                serializer = ProductSerializer(data=product)
                action = "Adding"

            if serializer.is_valid():
                serializer.save()
                print(f"{action} product: ", product["title"])
            else:
                raise Exception("Error validating the product data", serializer.errors)
        except Exception as e:
            print(e)
            print("Error processing sample data on product: ", product["title"])
            return

    print("Sample data processed successfully!")
