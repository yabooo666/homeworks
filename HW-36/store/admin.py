from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "has_discount", "discount_price", "is_available")
    list_filter = ("has_discount", "is_available", "category")
    search_fields = ("name", "description")
    list_editable = ("price", "has_discount", "is_available")
