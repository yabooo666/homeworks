# დეკორატორი 1 ლარიანი საკომისიოსა და ბალანსის შემოწმებისთვის
def apply_fee(func):
    def wrapper(balance, amount):
        total = amount + 1  # თანხა + 1 ლარი საკომისიო
        if balance < total:
            return "შეცდომა: ანგარიშზე არ არის საკმარისი თანხა (საკომისიო 1 ლარი)!"
        return func(balance, total)
    return wrapper


@apply_fee
def transaction(balance, amount):
    return balance - amount


# დემონსტრაცია
if __name__ == "__main__":
    print("დარჩენილი ბალანსი (100 - 50 - 1):", transaction(100, 50))
    print(transaction(20, 20))  # არასაკმარისი ბალანსი (20 < 21)
