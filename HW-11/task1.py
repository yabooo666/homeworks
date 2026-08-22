# ფაილის ანალიზი: ხაზების რაოდენობა, ყველაზე გრძელი ხაზი, სიტყვების რაოდენობა
def analyze_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
        f.seek(0)
        content = f.read()
    
    line_count = len(lines)
    longest_line = max(lines, key=len) if lines else ""
    word_count = len(content.split())
    return line_count, longest_line, word_count

filename = input("შეიყვანეთ ფაილის დასახელება: ")
lines, longest, words = analyze_file(filename)

print(f"ხაზების რაოდენობა: {lines}")
print(f"ყველაზე გრძელი ხაზი: {longest}")
print(f"სიტყვების რაოდენობა: {words}")
