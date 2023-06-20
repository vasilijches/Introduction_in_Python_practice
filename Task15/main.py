# 1
# from random import randint
# N = int(input('Введите число: '))
#
# i = 1
# min_w, max_w = 0, 0
#
# while i <= N:
#     weight = randint(1, 20)
#     print(weight, end=' ')
#     if i == 1
#         min_w, max_w = weight
#     if weight < min_w:
#         min_w = weight
#     elif weight > max_w:
#         max_w = weight
#     i += 1
#
# print()
# print(min_w, max_w)

# 2
# from random import randint
# N = int(input('Введите число: '))
#
# i = 1
# min_lim, max_lim = 0, 20
# min_w, max_w = max_lim, min_lim
#
# while i <= N:
#     weight = randint(min_lim, max_lim)
#     print(weight, end=' ')
#     if weight < min_w:
#         min_w = weight
#     if weight > max_w:
#         max_w = weight
#     i += 1
#
# print()
# print(min_w, max_w)

# 3
import random

min_ = float('inf')  # абсолютный (бесконечный) максимум
max_ = float('-inf')  # абсолютный (бесконечный) минимум

for _ in range(int(input('Count: '))):
    weight = random.randint(1, 20)
    print(weight, end=' ')
    if weight > max_:
        max_ = weight
    if weight < min_:
        min_ = weight

print(f'\n\n{min_=} {max_=}')
