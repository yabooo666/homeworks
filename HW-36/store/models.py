from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="კატეგორიის სახელი")
    description = models.TextField(blank=True, verbose_name="აღწერა")
    visit_count = models.PositiveIntegerField(default=0, verbose_name="ნახვების რაოდენობა")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="კატეგორია"
    )
    name = models.CharField(max_length=150, verbose_name="პროდუქტის დასახელება")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="აღწერა")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ფასი")
    has_discount = models.BooleanField(default=False, verbose_name="აქვს ფასდაკლება (SALE)")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="ფასდაკლებული ფასი")
    is_available = models.BooleanField(default=True, verbose_name="ხელმისაწვდომია")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="სურათი")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="დამატების თარიღი")

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return self.name
