# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4, 7]
# print(len(set(list_1)))

# from random import randint
#
# list_1 = [randint(1,10) for i in range(10)]
# print(list_1)
# print(set(list_1))
# print(len(set(list_1)))

# from random import randint
#
# list_1 = [randint(1,10) for i in range(10)]
# print(list_1)
# # list_1.sort()
#
# for i in range(len(list_1)):
#     for k in range(i+1, len(list_1)):
#         if list_1[i] > list_1[k]:
#             list_1[i], list_1[k] = list_1[k], list_1[i]
#
# print(list_1)
#
# i = 0
# while i < len(list_1) - 1:
#     if list_1[i] == list_1[i+1]:
#         list_1.pop(i)
#     else:
#         i += 1
#
# print(list_1)
# print(len(list_1))

import random
print(my_list := [random.randint(0, 10) for _ in range(10)])
print(len(set(my_list)))