# მთავარი კლასი Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = max(0, salary)  # ხელფასი არ უნდა იყოს უარყოფითი

    def show_info(self):
        print(f"თანამშრომელი: {self.name}, ხელფასი: {self.salary}")

    def work(self):
        print("Employee is working")

    def raise_salary(self, amount):
        if amount > 0:
            self.salary += amount


# შვილობილი კლასი Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print("Writing code...")

    def work(self):
        print("Developer is coding")


# შვილობილი კლასი Designer
class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def create_design(self):
        print("Creating design...")

    def work(self):
        print("Designer is designing")


# დემონსტრაცია
if __name__ == "__main__":
    dev = Developer("Nika", 3500, "Python")
    dev.show_info()
    dev.work()
    dev.code()
    dev.raise_salary(500)
    print(f"გაზრდილი ხელფასი: {dev.salary}\n")

    des = Designer("Ana", 2800, "Figma")
    des.show_info()
    des.work()
    des.create_design()
    des.raise_salary(300)
    print(f"გაზრდილი ხელფასი: {des.salary}")
