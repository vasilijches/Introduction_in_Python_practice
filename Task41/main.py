# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел
from random import randint

print(list_1 := [randint(1, 10) for _ in range(int(input('Enter list length: ')))])


# def max_counting(l: list) -> int:
#     count = 0
#     for i in range(len(l)):
#         if l[0] < l[1] > l[2]:
#             count += 1
#         l.append(l.pop(0))
#     return count


# print(max_counting(list_1))


# var2
# print(len([list_1[i] for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[i + 1]]))
# var3
print(len([0 for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[i + 1]]))
