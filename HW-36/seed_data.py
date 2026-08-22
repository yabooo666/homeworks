import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from store.models import Category, Product

# ბაზის გასუფთავება
Product.objects.all().delete()
Category.objects.all().delete()

# კატეგორიების შექმნა
cat_laptops = Category.objects.create(name="Laptops", description="ლეპტოპები და ულტრაბუქები")
cat_phones = Category.objects.create(name="Smartphones", description="სმარტფონები და აქსესუარები")
cat_audio = Category.objects.create(name="Audio & Headphones", description="ყურსასმენები და დინამიკები")
cat_accessories = Category.objects.create(name="Accessories", description="კლავიატურები, მაუსები და ჰაბები")
cat_empty = Category.objects.create(name="Cameras & Drones", description="ცარიელი კატეგორია ტესტირებისთვის") # არ აქვს პროდუქტი

# პროდუქტების შექმნა (დალაგებული სხვადასხვა ფასებით და SALE სტატუსებით)
products_data = [
    # Accessories
    {"category": cat_accessories, "name": "USB-C to HDMI Adapter", "desc": "4K 60Hz უმაღლესი ხარისხის ადაპტერი", "price": 25.00, "has_discount": False, "discount_price": None},
    {"category": cat_accessories, "name": "Wireless Ergonomic Mouse", "desc": "Bluetooth 5.0 ერგონომიული მაუსი", "price": 45.00, "has_discount": True, "discount_price": 35.00},
    {"category": cat_accessories, "name": "Mechanical Gaming Keyboard", "desc": "RGB განათებით და Red Switch-ებით", "price": 89.00, "has_discount": True, "discount_price": 69.00},

    # Audio
    {"category": cat_audio, "name": "JBL Flip 6 Speaker", "desc": "წყალგაუმტარი პორტატული დინამიკი", "price": 120.00, "has_discount": False, "discount_price": None},
    {"category": cat_audio, "name": "Sony WH-1000XM5 Headphones", "desc": "ხმაურის ჩამხშობი პრემიუმ ყურსასმენი", "price": 380.00, "has_discount": True, "discount_price": 299.00},
    {"category": cat_audio, "name": "Apple AirPods Pro 2", "desc": "MagSafe ქეისით და USB-C პორტით", "price": 249.00, "has_discount": False, "discount_price": None},

    # Smartphones
    {"category": cat_phones, "name": "Google Pixel 8a", "desc": "128GB, საუკეთესო კამერა და AI ფუნქციები", "price": 499.00, "has_discount": True, "discount_price": 429.00},
    {"category": cat_phones, "name": "Samsung Galaxy S24 Ultra", "desc": "256GB Titanium Gray, S-Pen მხარდაჭერით", "price": 1199.00, "has_discount": False, "discount_price": None},
    {"category": cat_phones, "name": "iPhone 16 Pro", "desc": "128GB Natural Titanium, A18 Pro ჩიპი", "price": 1099.00, "has_discount": False, "discount_price": None},

    # Laptops
    {"category": cat_laptops, "name": "Lenovo ThinkPad E14", "desc": "Intel Core i5, 16GB RAM, 512GB SSD", "price": 750.00, "has_discount": True, "discount_price": 649.00},
    {"category": cat_laptops, "name": "ASUS ROG Zephyrus G14", "desc": "Ryzen 9, RTX 4070, 32GB RAM, OLED 120Hz", "price": 1850.00, "has_discount": True, "discount_price": 1699.00},
    {"category": cat_laptops, "name": "MacBook Pro 14 M3 Pro", "desc": "18GB Unified Memory, 512GB SSD Space Black", "price": 1999.00, "has_discount": False, "discount_price": None},
]

for p in products_data:
    Product.objects.create(
        category=p["category"],
        name=p["name"],
        description=p["desc"],
        price=p["price"],
        has_discount=p["has_discount"],
        discount_price=p["discount_price"],
        is_available=True,
    )

print(f"ბაზა შეივსო: {Category.objects.count()} კატეგორია და {Product.objects.count()} პროდუქტი.")
