from .models import Product


def latest_products_processor(request):
    """
    გლობალური Context Processor:
    პროექტში არსებულ ყველა HTML ფაილში ხელმისაწვდომს ხდის ცვლადს `latest_products`
    (ბოლოს დამატებული 5 პროდუქტი)
    """
    return {
        "latest_products": Product.objects.filter(is_available=True).order_by("-created_at")[:5]
    }
