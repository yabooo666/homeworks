import random

# შემთხვევითი რიცხვი და სიცოცხლეები
target = random.randint(1, 100)
lives = 5

print("გამოიცანით რიცხვი 1-დან 100-მდე! (5 სიცოცხლე)")

while lives > 0:
    guess = int(input(f"შეიყვანეთ რიცხვი (დარჩენილი სიცოცხლე: {lives}): "))
    
    if guess == target:
        print("გილოცავთ, თქვენ მოიგეთ!")
        break
    
    lives -= 1
    hint = "მეტია" if target > guess else "ნაკლებია"
    print(f"ჩაფიქრებული რიცხვი {hint} თქვენს რიცხვზე!")

if lives == 0:
    print(f"სამწუხაროდ წააგეთ! ჩაფიქრებული რიცხვი იყო: {target}")
