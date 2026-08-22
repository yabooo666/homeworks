from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductForm
from .models import Category, Product


# Helper: არაცარიელი კატეგორიები რაოდენობით
def get_non_empty_categories():
    return Category.objects.annotate(product_count=Count("products")).filter(product_count__gt=0)


# 1. მთავარი გვერდი (Search + Filter + Sort + Pagination)
class HomeView(ListView):
    model = Product
    template_name = "store/home.html"
    context_object_name = "products"
    paginate_by = 6  # 6 პროდუქტი თითო გვერდზე

    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True)

        # 1.1 ძებნა (Search)
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))

        # 1.2 კატეგორიის ფილტრი
        category_id = self.request.GET.get("category", "").strip()
        if category_id and category_id.isdigit():
            queryset = queryset.filter(category_id=int(category_id))

        # 1.3 მინიმალური ფასი
        min_price = self.request.GET.get("min_price", "").strip()
        if min_price:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                pass

        # 1.4 მაქსიმალური ფასი
        max_price = self.request.GET.get("max_price", "").strip()
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass

        # 1.5 ფასდაკლების ფილტრი
        on_sale = self.request.GET.get("on_sale", "").strip()
        if on_sale == "1" or on_sale.lower() == "true":
            queryset = queryset.filter(has_discount=True)

        # 1.6 სორტირება
        sort = self.request.GET.get("sort", "price_asc").strip()
        sort_mapping = {
            "price_asc": "price",
            "price_desc": "-price",
            "newest": "-created_at",
            "name_asc": "name",
            "name_desc": "-name",
        }
        order_field = sort_mapping.get(sort, "price")
        queryset = queryset.order_by(order_field)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_non_empty_categories()

        # აქტიური ფილტრების პარამეტრები
        context["current_q"] = self.request.GET.get("q", "").strip()
        context["current_category"] = self.request.GET.get("category", "").strip()
        context["current_min_price"] = self.request.GET.get("min_price", "").strip()
        context["current_max_price"] = self.request.GET.get("max_price", "").strip()
        context["current_on_sale"] = self.request.GET.get("on_sale", "").strip()
        context["current_sort"] = self.request.GET.get("sort", "price_asc").strip()

        # URL Query პარამეტრები პაგინაციისთვის
        query_dict = self.request.GET.copy()
        if "page" in query_dict:
            del query_dict["page"]
        context["querystring"] = query_dict.urlencode()

        return context


# 2. კატეგორიის პროდუქტების გვერდი
class CategoryDetailView(HomeView):
    template_name = "store/category_detail.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs["category_id"])
        queryset = super().get_queryset()
        return queryset.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


# 3. ფასდაკლებული პროდუქტების გვერდი (SALE)
class SalesListView(HomeView):
    template_name = "store/sales.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(has_discount=True)


# 4. პროდუქტის დეტალური გვერდი
class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_non_empty_categories()
        return context


# 5. ახალი პროდუქტის დამატება
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_form.html"

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_non_empty_categories()
        context["title"] = "ახალი პროდუქტის დამატება"
        context["button_text"] = "პროდუქტის შექმნა"
        return context


# 6. პროდუქტის რედაქტირება
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_form.html"

    def get_success_url(self):
        return reverse_lazy("product_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_non_empty_categories()
        context["title"] = f"რედაქტირება: {self.object.name}"
        context["button_text"] = "ცვლილებების შენახვა"
        return context


# 7. პროდუქტის წაშლა
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = get_non_empty_categories()
        return context
