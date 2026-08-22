from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

# filter: ფასი < 100
under_100 = list(filter(lambda p: p["price"] < 100, products))
print("ფასი < 100:", under_100)

# map: სახელი და ფასი
names_prices = list(map(lambda p: f"{p['name']}: {p['price']}", products))
print("სახელი და ფასი:", names_prices)

# sorted: დალაგებული ფასით
sorted_products = sorted(products, key=lambda p: p["price"])
print("დალაგებული ფასით:", sorted_products)

# reduce: ფასების ჯამი
total_sum = reduce(lambda acc, p: acc + p["price"], products, 0)
print("ფასების ჯამი:", total_sum)
