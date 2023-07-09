# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает)

# def dividers_sum(number):
#     res = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             res += i
#     return res
#
#
# # print({(j, dividers_sum(j)) for j in range(10000) if j < dividers_sum(j)
# #           and j == dividers_sum(dividers_sum(j))})
#
# for j in range(100000):
#     k = dividers_sum(j)
#     if j < k and j == dividers_sum(k):
#         print(j, k)

def div_sum(number: int) -> int:
    return sum([div for div in range(1, number // 2 + 1) if not number % div])


div_sum_dict = {num: div_sum(num) for num in range(50000)}

for num, summ in div_sum_dict.items():
    if num == div_sum_dict.get(summ) and num < summ:
        print(num, summ)