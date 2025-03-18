from django.urls import path

from products.views import (
    ProductListView,
    CategoriesListView,
    PriceRangeView,
    SalesChartView,
    ItemsChartView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("list", ProductListView.as_view(), name="product-list"),
    path("add", ProductCreateView.as_view(), name="product-add"),
    path("<int:pk>", ProductUpdateView.as_view(), name="product-update"),
    path("<int:pk>/delete", ProductDeleteView.as_view(), name="product-delete"),
    path("price_range", PriceRangeView.as_view(), name="price-range"),
    path("categories", CategoriesListView.as_view(), name="categories-list"),
    path("sales_chart", SalesChartView.as_view(), name="sales-chart"),
    path("items_chart", ItemsChartView.as_view(), name="items-chart"),
]
