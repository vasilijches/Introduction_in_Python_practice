# Напишите программу для печати всех уникальных
# значений в словаре.

# dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
#           {"V": "S009"}, {"VIII": "S007"}]
# for i in range(len(dict_1)):
#     for (j, k) in dict_1[i].items():
#         print(k, end=' ')
#
# print(list(k for i in range(len(dict_1)) for (j, k) in dict_1[i].items()))

# for item in dict_1:
#     for v in item.values():
#         print(v, end=' ')

# s1 = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'.split(', ')
# for i in range(len(s1)):
#     print("\'" + s1[i] + "\': 1,", end=' ')

k = "ноутбук"
def scrabble_score(key):
    dict_1 = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'D': 2, 'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4,
        'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'J': 8, 'X': 8, 'Ш': 8, 'Э': 8, 'Ю': 8,
        'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
    list_1 = list(k.upper())
    return sum(dict_1[list_1[i]] for i in range(len(list_1)))


print(scrabble_score(k))
