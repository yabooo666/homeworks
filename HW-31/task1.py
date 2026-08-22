import os
import random
from pymongo import MongoClient

# MongoDB კავშირის პარამეტრები
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://yaboia:UdzlieresiParoliRomelicGithubZeSajarodDaidebaDaVnaxoTVincIpovnisRasIzavs@5.83.153.60:5009/shop?authSource=homework30-shop"
)

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client["shop"]
collection = db["products"]

# 1. 50 პროდუქტის გენერირება
categories = ["Electronics", "Books", "Clothes"]
products = []

for i in range(1, 51):
    qty = random.randint(0, 100)
    products.append({
        "name": f"Product {i}",
        "category": random.choice(categories),
        "price": random.randint(50, 3000),
        "quantity": qty,
        "available": qty > 0,
    })

# ძველი მონაცემების გასუფთავება და ახალი 50 პროდუქტის შეტანა
collection.delete_many({})
collection.insert_many(products)
print("50 პროდუქტი წარმატებით ჩაიწერა MongoDB-ში!\n")

# 2. ყველა პროდუქტის დაბეჭდვა
print("=== 1. ყველა პროდუქტი ===")
for p in collection.find({}, {"_id": 0}):
    print(p)

# 3. მხოლოდ ხელმისაწვდომი პროდუქტები
print("\n=== 2. ხელმისაწვდომი პროდუქტები (available = True) ===")
for p in collection.find({"available": True}, {"_id": 0}):
    print(p)

# 4. პროდუქტები, რომლის ფასი მეტია 1000-ზე
print("\n=== 3. პროდუქტები, რომლის ფასი > 1000 ===")
for p in collection.find({"price": {"$gt": 1000}}, {"_id": 0}):
    print(p)

# 5. პროდუქტების რაოდენობის დათვლა თითო კატეგორიაში
print("\n=== 4. პროდუქტების რაოდენობა კატეგორიების მიხედვით ===")
pipeline = [
    {"$group": {"_id": "$category", "total_products": {"$sum": 1}}}
]
for cat in collection.aggregate(pipeline):
    print(f"კატეგორია: {cat['_id']} -> {cat['total_products']} პროდუქტი")

# 6. ერთ-ერთი პროდუქტის რაოდენობის შეცვლა (მაგ. Product 1)
print("\n=== 5. Product 1-ის რაოდენობის შეცვლა ===")
new_qty = 88
collection.update_one(
    {"name": "Product 1"},
    {"$set": {"quantity": new_qty, "available": new_qty > 0}}
)
updated_product = collection.find_one({"name": "Product 1"}, {"_id": 0})
print("განახლებული Product 1:", updated_product)
