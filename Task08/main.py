"""
Задача 8: Требуется определить,
 можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками
  (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

print("Введите размеры шоколадной плитки в дольках")
n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
k = int(input("Введите, сколько долек собираетесь отломить: "))

print(n, m, k, end=" -> ")
if k < n * m and (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")