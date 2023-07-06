# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

number_n = int(input('Enter length: '))

# def reverse__numb_sequence(n):
#     if n == 0:
#         return
#     m = input('Enter number: ')
#     reverse__numb_sequence(n - 1)
#     print(m, end=' ')
#
#
# reverse__numb_sequence(number_n)


# def reverse__numb_sequence(num: int) -> str:
#     if num == 0:
#         return ''
#     char = input('Enter a char: ')
#     return reverse__numb_sequence(num - 1) + char
#
#
# print(reverse__numb_sequence(number_n))

# Обратная задача, то есть выводит в прямом порядке, а  не в обратном

# def reverse__numb_sequence(num: int) -> str:
#     if num == 0:
#         return ''
#     char = input('Enter a char: ')
#     return char + reverse__numb_sequence(num - 1)
#
#
# print(reverse__numb_sequence(number_n))
