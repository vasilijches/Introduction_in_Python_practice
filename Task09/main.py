# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

N = int(input('Введите число'))

fact = 1
while N > 0:
    fact *= N
    N -= 1

print(fact)