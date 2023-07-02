# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint
# list_1 = [randint(-10,10) for _ in range(20)]
#
# print(list_1)
#
# count = 0
# for i in range(len(list_1)-1):
#     count += 1 if list_1[i] < list_1[i+1] else 0
# print(count)

print(list_1 := [randint(-10,10) for _ in range(20)])
print(len([i for i in range(1, len(list_1)) if list_1[i-1] < list_1[i]]))
