# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии

def power(num: int, deg: int):
    if deg == 0:
        return 1
    return num * power(num, deg - 1)

num_a = int(input('Enter number A: '))
num_b = int(input('Enter number B: '))

print(f'{num_a} ^ {num_b} = {power(num_a, num_b)}')
