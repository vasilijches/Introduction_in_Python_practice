# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

text = 'a a a b c a a d c d d'

# list_1 = text.split()
# list_2 = list(set(list_1))
#
# count = 0
# for i in range(len(list_2)):
#     for j in range(len(list_1)):
#         if list_1[j] == list_2[i]:
#             if count > 0:
#                 list_1[j] += f'_{count}'
#             count += 1
#     count = 0
# print(' '.join(list_1))

# temp = {}
# result = ''
# for i in range(len(text)):
#     if text[i] not in temp.keys():
#         temp[text[i]] = 1
#         result += f'{text[i]}'
#     else:
#         result += f'{text[i]}_{temp[text[i]]} '
#         temp[text[i]] += 1
# print(result)

numbers = '1234567890123492873'

dict_count = {}

for num in numbers:
    dict_count[num] = dict_count.get(num, 0) + 1
    if dict_count.get(num) < 2:
        print(num, end=' ')
    else:
        print(f'{num}_{dict_count.get(num) - 1}', end=' ')