# კენტი და ლუწი რიცხვების გაყოფა ორ ლისტად
def split_odd_even(*args):
    odds = [x for x in args if x % 2 != 0]
    evens = [x for x in args if x % 2 == 0]
    return odds, evens

odds, evens = split_odd_even(1, 2, 3, 4, 5, 6, 7, 8)
print(f"კენტები: {odds}")
print(f"ლუწები: {evens}")
