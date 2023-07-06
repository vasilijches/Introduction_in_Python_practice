# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# numb = int(input('Enter number:'))
# print(is_prime(numb))

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print('Complex')
#             return
#     print('Prime')
#
#
# numb = int(input('Enter number:'))
# is_prime(numb)

# def is_prime(num: int) -> bool:
#     for i in range(2, num//2 + 1):
#         if num%i == 0:
#             return False
#     return True
#
# numb = int(input('Enter number:'))
# is_prime(numb)

# numb = int(input('Enter number:'))
#
#
# def is_prime(num: int) -> bool:
#     if num in (1, 2):
#         return True
#     if num % 2 == 0:
#         return False
#     for div in range(3, int(num ** 0.5) + 1, 2):
#         if num % div == 0:
#             return False
#     return True
#
#
# print(is_prime(numb))
