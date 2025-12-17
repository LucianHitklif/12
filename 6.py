word = input("Введите слово: ")

print(*word, sep=',')

word1 = word[::1]

if word1 == word:
    print("Это палиндром")
else:
    print("Не палиндром")
