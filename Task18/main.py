# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X


N = int(input('Enter N: '))
print(A := [i for i in range(N)])

X = float(input('Enter X: '))
diff_list = [abs(X - i) for i in range(N)]
res = A[diff_list.index(min(diff_list))]

print(res)
