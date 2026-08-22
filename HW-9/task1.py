# რიცხვების შეყვანა და დაჯამება (ნაგულისხმევი 5)
def sum_numbers(count=5):
    return sum(float(input(f"შეიყვანეთ რიცხვი ({i+1}/{count}): ")) for i in range(count))

total = sum_numbers()
print(f"საბოლოო ჯამი: {total}")
