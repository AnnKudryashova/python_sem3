# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
#45 -> 101101
#3 -> 11
#2 -> 10

X = int(input('Введите десятичное число X: '))
def Binary(X):
    binary_number = [0] * X
    i = 0
    while X > 0:
        binary_number[i] = X % 2
        X = X//2
        i += 1

    for j in range (i-1, -1, -1):
        print(binary_number[j], end = " ")

Binary(X)