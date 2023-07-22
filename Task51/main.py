# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику
# import random
#
# print(data := [random.randint(1, 150) for _ in range(20)])
#
#
# # def same_by(characteristic, objects):
# #     lst = list(map(characteristic, objects))
# #     return len(lst) == sum(lst)

data = ['ssse', 'eeee', 'wwww', 'tttt']
def same_by(characteristic, objects):
    return len(objects) == len(list(filter(characteristic, objects)))


print(same_by(lambda x: len(x) == 4, data))
