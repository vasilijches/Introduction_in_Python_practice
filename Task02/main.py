"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

n = int(input("Введите трёхзначное число: "))


# Вариант1
# n = int(n)
# result = n // 100 + (n % 100) // 10 + n % 10
# print(f"Сумма цифр числа {n} равна {result}")

# Вариант2(универсальный)
# result = 0
# for i in n:
#     result += int(i)
# print(f"Сумма цифр числа {n} равна {result}")

# Вариант3(универсальный)
# n2 = int(n)
# result = 0
# while n2 > 0:
#     result += n2 % 10
#     n2 //= 10
# print(f"Сумма цифр числа {n} равна {result}")

# Вариант4(универсальный с рекурсией)
# def sum_digit(number: int) -> int:
#     if number == 0:
#         return number
#     return number % 10 + sum_digit(number // 10)
#
#
# n = int(n)
# result = sum_digit(n)
# # print(f"Сумма цифр числа {n} равна {result}")
