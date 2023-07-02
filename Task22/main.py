# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества.Затем пользователь вводит сами элементы множеств.

from random import randint

N = int(input('Enter the first number: '))
list_1 = [randint(-N // 2, N // 2) for _ in range(N + 1)]

M = int(input('Enter the second number: '))
list_2 = [randint(-M // 2, M // 2) for _ in range(M + 1)]

list_3 = set(list_1 + list_2) - (set(list_1) - set(list_2)) - (set(list_2) - set(list_1))
list_3 = list(list_3)
list_3.sort()

print(list_3)
