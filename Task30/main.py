# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

import random

el_1 = random.randint(-5, 5)
step = random.randint(-5, 5)
size = random.randint(0, 10)

print(f'{el_1} + ({size} - 1) * {step}: ')
print([el_1 + i * step for i in range(size)])