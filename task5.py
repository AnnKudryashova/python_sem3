#Задайте число - размер списка. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13]
# [Негафибоначчи]

x = int(input('Введите число: '))

def Fibonacci(x):
    numbers = []
    a = 1
    b = 1
    for i in range (x-1):
        numbers.append(a)
        a, b = b, a + b
    a = 0
    b = 1
    for i in range (x):
        numbers.insert(0, a)
        a, b = b, a - b
    return numbers

numbers = Fibonacci(x)
print(Fibonacci(x))