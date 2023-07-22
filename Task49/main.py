# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
#
# # def find_farthest_orbit(lst: list):
# #     res_lst = [item for item in lst if item[0] != item[1]]
# #     res_lst = list(map(lambda x: x[0] * x[1], res_lst))
# #     max_s = max(res_lst)
# #     res_lst = list(enumerate(res_lst))
# #     res_lst = list(filter(lambda x: x[1] == max_s, res_lst))
# #     return res_lst
#
# def find_farthest_orbit(lst: list):
#     data = list(filter(lambda x: not x[0] == x[1], orbits))
#     res = list(map(lambda x: x[0] * x[1], data))
#     return lst[res.index(max(res))]
#
#
# print(*find_farthest_orbit(orbits))
import random

MIN_SIZE = 1
MAX_SIZE = 10
PLANETS = 15


def planets_data(min_size: int, max_size: int, planet: int) -> list[tuple[int, int]]:
    def ellipse(mins: int, maxs: int, count: int):
        return [random.randint(mins, maxs) for _ in range(count)]

    return list(zip(ellipse(min_size, max_size, planet), ellipse(min_size, max_size, planet)))


print(all_planets := planets_data(MIN_SIZE, MAX_SIZE, PLANETS))

print(all_planets := list(filter(lambda x: x[0] != x[1], all_planets)))
print(max(all_planets, key=lambda x: x[0] * x[1]))
