word = input("Введите слово: ")

line = list(word)
rev_line = line[::-1]

if line == rev_line:
    print("Это палиндром")
else:
    print("Не палиндром")
