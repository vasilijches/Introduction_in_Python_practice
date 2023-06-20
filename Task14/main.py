# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

# Вариант 1(мой)
# from random import randint
#
# N = randint(1, 1024)
# print(N, "->", end=' ')
#
# num_1 = 1
# while num_1 <= N:
#     print(num_1, end=' ')
#     num_1 *= 2

# Вариант 2
n = int(input('Enter the number: '))
i = 0
while 2**i <= n:
    print(2**i, end=' ')
    i += 1