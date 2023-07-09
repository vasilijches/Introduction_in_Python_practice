# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# from collections import Counter
# import random as rnd
#
# print(list_1 := [rnd.randint(0,10) for _ in range(10)])
#
# print(c := Counter(list_1).values())
# print(sum([i // 2 for i in Counter(list_1).values()]))

# import random
#
# print(list_1 := [random.randint(0,10) for _ in range(10)])
#
# dict_1 = dict((item, list_1.count(item)) for item in set(list_1))
# print(sum(v // 2 for v in dict_1.values()))

# import random
#
# print(list_1 := [random.randint(0,10) for _ in range(10)])
# list_1.sort()
# print(list_1)
#
# count = i = 0
# while i < len(list_1) - 1:
#     if list_1[i] == list_1[i + 1]:
#         count += 1
#         i += 2
#     else:
#         i += 1
# print(count)

import random

print(list_1 := [random.randint(0,10) for _ in range(10)])

print(sum([list_1.count(item) // 2 for item in set(list_1)]))
