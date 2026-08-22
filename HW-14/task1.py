class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
        self.status = Student.status
        self.pay = Student.pay

    # სრული სახელი და გვარი
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # ფასდაკლება 18 წლამდე (-20%)
    def get_discount(self):
        if self.age < 18:
            self.pay *= 0.8
        return self.pay

    # საშუალო ქულის გამოთვლა
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    # შეფასების სტატუსი
    def get_status(self):
        avg = self.calculate_average()
        if avg > 90:
            return "Excellent"
        elif avg >= 70:
            return "Good"
        elif avg >= 50:
            return "Average"
        else:
            self.status = False
            return "Poor"


# დემონსტრაცია
if __name__ == "__main__":
    s1 = Student("Giorgi", "Kabanashvili", 17, [95, 92, 98])
    print(s1.get_full_name())
    print(f"გადასახადი: {s1.get_discount()}")
    print(f"საშუალო: {s1.calculate_average():.2f}")
    print(f"სტატუსი: {s1.get_status()} (status={s1.status})\n")

    s2 = Student("Zviangi", "Shavkverashvili", 20, [40, 45, 30])
    print(s2.get_full_name())
    print(f"სტატუსი: {s2.get_status()} (status={s2.status})")
