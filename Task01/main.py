"""
Задача №1
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
"""

n = 700
m = 799

day1 = m // n + (m % n != 0)
day2 = (m + n - 1)//n

print(day1)
print(day2)