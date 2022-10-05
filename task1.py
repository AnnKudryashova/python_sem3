# Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random
N = int(input('введите число N: '))
list = []
for i in range(N):
    list.append(random.randint(-10, 10))

def Summ(list):
    S = 0
    for i in range (0, len(list)):
        if i%2 != 0:
            S += list[i]
    return S
    
print(f"{list} -> сумма элементов на нечётных позициях: {Summ(list)}")