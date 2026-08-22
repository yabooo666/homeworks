import re

# სიტყვის სიხშირის დათვლა ფაილში
def count_word_in_file(filename, word):
    with open(filename, "r", encoding="utf-8") as f:
        words = re.findall(r"\b\w+\b", f.read().lower())
        return words.count(word.lower())

filename = input("შეიყვანეთ ფაილის დასახელება: ")
word = input("შეიყვანეთ საძიებო სიტყვა: ")

count = count_word_in_file(filename, word)
print(f"სიტყვა '{word}' გვხვდება {count}-ჯერ")
