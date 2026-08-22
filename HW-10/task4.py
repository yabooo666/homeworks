# რეკურსიული ჯამი 1-დან n-მდე
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

n = int(input("შეიყვანეთ რიცხვი: "))
print(f"ჯამი 1-დან {n}-მდე: {recursive_sum(n)}")
