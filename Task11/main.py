# Задача №11. Решение в группах
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# A = int(input('Введите число: '))
#
# fib1 = 0
# fib2 = 1
# count = 1
# while fib2 < A:
#     fib2 += fib1
#     fib1 = fib2 - fib1
#     count += 1
# if A < fib2:
#     print(-1)
# else:
#     print(count)

fib_1, fib_2 = 0, 1
fib_n = int(input('Введите число Фибонначи: '))
index = 1
while fib_2 < fib_n:
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index += 1
print(index if fib_n == fib_2 else -1) # тернарный оператор
