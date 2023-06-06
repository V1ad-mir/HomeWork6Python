# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random
from random import randint
number_1 = int(input('Введите минимальный элемент диапазона: '))
number_2 = int(input('Введите максимальный элемент диапазона: '))
len_my_list = int(input('Введите колличество элементов: '))

my_list=[]
for i in range(len_my_list):
    my_list.append(randint(-10, 10))
print(my_list)
for i in range(len_my_list):
    if number_1<=my_list[i] and my_list[i]<=number_2:
        print(f'{i} ', end='')