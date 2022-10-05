#Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
N = int(input('введите число N: '))
list = []
for i in range(N):
    list.append(random.randint(-10, 10))
print(f"Исходный список: {list}")
print()

def New_list(list):
    new_list = []
    for i in range ((N+1)//2):
        new_list.append(list[i]*list[(N-1-i)])
    return new_list

print(f"Новый список с произведениями пар чисел: {New_list(list)}")