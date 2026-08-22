import csv
import os
import random
from faker import Faker

# Faker-ის ინიციალიზაცია
fake = Faker()
filepath = os.path.join(os.path.dirname(__file__), "persons.csv")

fields = ["ID", "first_name", "last_name", "age"]

# persons.csv-ში 50 პიროვნების ჩაწერა DictWriter-ით
with open(filepath, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    
    for i in range(1, 51):
        writer.writerow({
            "ID": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": random.randint(20, 80)
        })

print("persons.csv წარმატებით შეიქმნა 50 ჩანაწერით!")
