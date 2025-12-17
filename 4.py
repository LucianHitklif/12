marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

num5 = 0
num2 = 0

for mark in marks:
    if mark == 5:
        num5 += 1
    if mark == 2:
        num2 += 1

print(f"Количество пятерок: {num5}")
print(f"Количество двоек: {num2}")
