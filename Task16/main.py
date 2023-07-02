# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

N = int(input('Enter list size: '))
print(list_1 := [randint(-N//2, N//2) for _ in range(N)])

x = int(input('Enter X: '))
print(len([list_1[i] for i in range(len(list_1)) if list_1[i] == x]))
