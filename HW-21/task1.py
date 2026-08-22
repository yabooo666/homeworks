from concurrent.futures import ThreadPoolExecutor

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]


# ფუნქცია, რომელიც ამოწმებს არის თუ არა რიცხვი მარტივი
def is_prime(n):
    if n < 2:
        return n, False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return n, False
    return n, True


def main():
    # ნაკადებით პარალელურად გაშვება
    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, num_list)

    for num, prime in results:
        status = "მარტივია" if prime else "შედგენილია"
        print(f"{num}: {status}")


if __name__ == "__main__":
    main()
