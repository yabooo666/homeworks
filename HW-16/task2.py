# მეტაკლასი, რომელიც ამოწმებს რომ ყველა მეთოდი იწყებოდეს '_'-ით
class UnderscoreMethodMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_val in dct.items():
            if callable(attr_val) and not attr_name.startswith("_"):
                raise ValueError(f"მეთოდი '{attr_name}' არ არის ვალიდური! მეთოდის სახელი უნდა იწყებოდეს '_'-ით.")
        return super().__new__(cls, name, bases, dct)


# ვალიდური კლასის მაგალითი
class ValidClass(metaclass=UnderscoreMethodMeta):
    data = 100  # ატრიბუტი შემოწმებას არ ექვემდებარება

    def __init__(self):
        pass

    def _test(self):
        return "ვალიდური მეთოდი"


# დემონსტრაცია
if __name__ == "__main__":
    obj = ValidClass()
    print("ValidClass შეიქმნა წარმატებით:", obj._test())

    # არავალიდური კლასის შექმნის მცდელობა
    try:
        class InvalidClass(metaclass=UnderscoreMethodMeta):
            def test(self):
                pass
    except ValueError as e:
        print("დაიჭირა მოსალოდნელი შეცდომა:", e)
