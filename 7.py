numbers = [10, 20, 30, 40, 50]

search_num = int(input("Введите число для поиска: "))
found = False

for index in range(len(numbers)):
    if numbers[index] == search_num:
        print(f'Число {search_num} находится под индексом {index}')
        found = True
        break
if not found:
    print("Такого числа нет в списке")
