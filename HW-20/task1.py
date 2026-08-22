import json
import os
import random
from faker import Faker

fake = Faker()
base_dir = os.path.dirname(__file__)
all_students_file = os.path.join(base_dir, "students.json")
active_students_file = os.path.join(base_dir, "active_students.json")

# 1. 100 სტუდენტის გენერირება
students = [
    {
        "student_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "is_active": random.choice([True, False]),
    }
    for i in range(1, 101)
]

# 2. students.json ფაილში ჩაწერა
with open(all_students_file, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)

# 3. ფაილის წაკითხვა და აქტიური სტუდენტების გაფილტვრა
with open(all_students_file, "r", encoding="utf-8") as f:
    loaded_students = json.load(f)

active_students = [s for s in loaded_students if s["is_active"]]

# 4. active_students.json ფაილში ჩაწერა
with open(active_students_file, "w", encoding="utf-8") as f:
    json.dump(active_students, f, indent=4)

print(f"სულ დაგენერირდა: {len(students)} სტუდენტი (ჩაიწერა students.json-ში)")
print(f"აქტიური სტუდენტი: {len(active_students)} (ჩაიწერა active_students.json-ში)")
