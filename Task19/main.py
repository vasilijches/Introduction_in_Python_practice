# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
list_1 = [i for i in range(10)]

# print(list_1)
# k = 2
# for _ in range(k):
#     list_1.insert(0, list_1[-1])
#     list_1.pop()
# print(list_1)

# k = 2
# print(list_1[-k:] + list_1[:len(list_1)-k])

# k = 2
# for _ in range(k):
#     list_1.insert(0, list_1.pop())
# print(list_1)

k = 2
for i in range(len(list_1)):
    print(list_1[i-k]%len(list_1), end=' ')



