# გაყოფა კონკრეტული ერორების დაჭერით (ValueError, ZeroDivisionError)
def safe_divide():
    try:
        a = int(input("შეიყვანეთ I მთელი რიცხვი: "))
        b = int(input("შეიყვანეთ II მთელი რიცხვი: "))
        return a / b
    except ValueError:
        print("შეცდომა: შეიყვანეთ მხოლოდ მთელი რიცხვი!")
    except ZeroDivisionError:
        print("შეცდომა: ნულზე გაყოფა შეუძლებელია!")

res = safe_divide()
if res is not None:
    print(f"შედეგი: {res}")
