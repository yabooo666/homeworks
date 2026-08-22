# წამების შეყვანა
total_seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))

# საათი, წუთი, წამი
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} წამი არის {hours} საათი, {minutes} წუთი, {seconds} წამი")
