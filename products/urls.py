from django.urls import path

from .views import ProductListView, CategoriesListView, PriceRangeView

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("price_range", PriceRangeView.as_view(), name="price-range"),
    path("categories", CategoriesListView.as_view(), name="categories-list"),
]
