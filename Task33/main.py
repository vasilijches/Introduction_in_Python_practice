# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

print(rating_list := [random.randint(1, 10) for _ in range(5)])

# min_rating = min(rating_list)
# max_rating = max(rating_list)

# min_r = max_r = rating_list[0]
# for i in range(len(rating_list)):
#     if rating_list[i] > max_r:
#         max_r = rating_list[i]
#     if rating_list[i] < min_r:
#         min_r = rating_list[i]
#
# for i in range(len(rating_list)):
#     if rating_list[i] == max_r:
#         rating_list[i] = min_r
#
# print(rating_list)

max_mark = max(rating_list)
min_mark = min(rating_list)

# # var2.1
# print([i if i != max_mark else min_mark for i in rating_list])

# # var2.2
print([min_mark if i == max_mark else i for i in rating_list])
