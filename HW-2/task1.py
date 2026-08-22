# მონაცემების შეყვანა
weight = float(input("შეიყვანეთ წონა (კგ): "))
height = float(input("შეიყვანეთ სიმაღლე (მ): "))

# BMI გამოთვლა და შეფასება
bmi = weight / (height ** 2)

if bmi < 19:
    print(f"BMI: {bmi:.2f} - underweight")
elif bmi <= 25:
    print(f"BMI: {bmi:.2f} - normalweight")
else:
    print(f"BMI: {bmi:.2f} - overweight")
