import re

# სიტყვების სიხშირის დათვლა წინადადებაში
def count_words(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return {w: words.count(w) for w in words}

sentence = input("შეიყვანეთ წინადადება: ")
print(count_words(sentence))
