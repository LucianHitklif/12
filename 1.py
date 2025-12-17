n = int(input("Напишите число больше 0: "))

for numbers in range(1, n+1):
    if numbers % 2 == 1:
        print(numbers)
