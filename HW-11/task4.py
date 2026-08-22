import os

# persons.txt-ის გაყოფა ორ ფაილად (ასაკი < 50 და ასაკი > 50)
base_dir = os.path.dirname(__file__)
input_file = os.path.join(base_dir, "persons.txt")
under_file = os.path.join(base_dir, "under_50.txt")
over_file = os.path.join(base_dir, "over_50.txt")

with open(input_file, "r", encoding="utf-8") as f, \
     open(under_file, "w", encoding="utf-8") as f_under, \
     open(over_file, "w", encoding="utf-8") as f_over:
    for line in f:
        parts = line.strip().split(", ")
        if len(parts) >= 2 and parts[1].isdigit():
            age = int(parts[1])
            if age < 50:
                f_under.write(line)
            elif age > 50:
                f_over.write(line)

print("ფაილები 'under_50.txt' და 'over_50.txt' წარმატებით შეიქმნა!")
