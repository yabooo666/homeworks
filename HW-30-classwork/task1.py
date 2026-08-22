import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), "inventory.db")
sql_path = os.path.join(os.path.dirname(__file__), "schema.sql")


# 1. პროცედურა: პროდუქტისთვის რაოდენობის დაკლება
def reduce_stock(cursor, product_id, quantity_to_deduct):
    cursor.execute("""
        UPDATE products 
        SET quantity = MAX(0, quantity - ?) 
        WHERE id = ?
    """, (quantity_to_deduct, product_id))
    print(f"პროცედურა გამოიძახა: პროდუქტ #{product_id}-ს მოაკლდა {quantity_to_deduct} ცალი.")


with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    # სქემისა და ტრიგერების შექმნა
    with open(sql_path, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    # 2. მონაცემების შეტანა (სტატუსის მითითების გარეშე)
    print("=== მონაცემების შეტანა (სტატუსი ხელით არ შეგვყავს) ===")
    sample_products = [
        ("Gaming Laptop", 1500.00, 25),   # > 10 -> in stock
        ("Mechanical Keyboard", 80.00, 7), # 1-10 -> low stock
        ("Wireless Mouse", 30.00, 0),     # 0 -> out of stock
        ("Monitor 4K", 400.00, 15),       # > 10 -> in stock
        ("USB-C Hub", 25.00, 3),          # 1-10 -> low stock
    ]

    cursor.executemany(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        sample_products
    )
    conn.commit()

    # შედეგის გამოტანა ტრიგერის მუშაობის შემდეგ
    print("\nცხრილის მდგომარეობა შევსებისთანავე (ტრიგერმა დაუსეტა სტატუსი):")
    cursor.execute("SELECT id, name, price, quantity, status FROM products")
    for r in cursor.fetchall():
        print(f"#{r[0]} {r[1]:<22} | ფასი: ${r[2]:<7.2f} | რაოდენობა: {r[3]:<3} | სტატუსი: {r[4]}")

    # 3. პროცედურის გამოძახება და ტრიგერის ავტომატური რეაქცია
    print("\n=== პროცედურის გამოძახება (რაოდენობის დაკლება) ===")
    # Laptop-ს (25) ვაკლებთ 18-ს -> გახდება 7 (უნდა გახდეს low stock)
    reduce_stock(cursor, 1, 18)
    
    # Keyboard-ს (7) ვაკლებთ 7-ს -> გახდება 0 (უნდა გახდეს out of stock)
    reduce_stock(cursor, 2, 7)
    conn.commit()

    print("\nცხრილის მდგომარეობა პროცედურის გამოძახების შემდეგ (სტატუსი ავტომატურად განახლდა):")
    cursor.execute("SELECT id, name, price, quantity, status FROM products")
    for r in cursor.fetchall():
        print(f"#{r[0]} {r[1]:<22} | ფასი: ${r[2]:<7.2f} | რაოდენობა: {r[3]:<3} | სტატუსი: {r[4]}")
