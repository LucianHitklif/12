import random

numbers = [random.randint(1, 100) for num in range(5)]
print(f"Рандомные числа: {numbers}")

min_index = 0
min_value = numbers[0]

for i in range (1, len(numbers)):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_index = i

numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
print(numbers)
