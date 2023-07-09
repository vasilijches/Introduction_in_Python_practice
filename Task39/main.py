# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

from random import randint

print(list_1 := [randint(1,30) for _ in range(1, 15)])
print(list_2 := [randint(1,30) for _ in range(1, 15)])

# print(set_1 := set(list_1) - set(list_2))
#
# for i in range(len(list_1)):
#     if list_1[i] in set_1:
#         print(list_1[i], end=' ')

# for i in range(len(list_1)):
#     if list_1[i] not in list_2:
#         print(list_1[i], end=' ')

print([item for item in list_1 if item not in list_2])

# обратный вариант:
# for i in range(len(list_1)):
#     if list_1[i] not in list_2:
#         print(list_1[i], end=' ')
