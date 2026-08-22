# სახელებისა და გვარების ჩაწერა ფაილში ნუმერაციით
filename = "users.txt"
count = 1

with open(filename, "w", encoding="utf-8") as f:
    while True:
        first_name = input("Enter your first name: ").strip()
        if first_name.lower() == "stop":
            break
        last_name = input("Enter your last name: ").strip()
        f.write(f"{count}. {first_name} {last_name}\n")
        count += 1

print(f"მონაცემები წარმატებით ჩაიწერა ფაილში '{filename}'")
