from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("category/<int:category_id>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("sales/", views.SalesListView.as_view(), name="sales"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", views.ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
]
