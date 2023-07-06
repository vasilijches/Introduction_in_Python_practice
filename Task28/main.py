# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать цикл

import random as rnd


def summa(a: int, b: int) -> int:
    if a == 0:
        return 0
    return 1 + summa(a - 1, b) if b == 0 else 1 + summa(b, a - 1)


num_a = rnd.randint(0, 10)
num_b = rnd.randint(0, 10)

print(num_a, '+', num_b, '=', summa(num_a, num_b))
