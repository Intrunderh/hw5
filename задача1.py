# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def stepen(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return (a * stepen(a, b - 1))
    
a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(f'Результат возведения в степень равен = {stepen(a, b)}')

# def stepen(a, b):
#     if b == 0:
#         return 1
#     if b == 1:
#         return a
#     else:
#         b = a**b
#         return b

# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(f'Результат возведения в степень равен = {stepen(a, b)}')