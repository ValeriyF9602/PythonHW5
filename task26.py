'''
Задача 26

Напишите программу, которая на вход принимает 
два числа A и B, и возводит число А в целую степень B с 
помощью рекурсии.

    A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''


def Exponentiation(x, y):
    if y == 0: return 1
    elif y > 0: return Exponentiation(x, y - 1) * x
    else: return 1 / (Exponentiation(x, -y - 1) * x)


a = int(input('Введите число: '))
b = int(input('Введите степень: '))

print(Exponentiation(a, b))
