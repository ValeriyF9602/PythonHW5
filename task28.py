'''
Задача 28

Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

    2 2
    4
'''


def summa(x, y):
    if y == 0:
        return x
    return summa(x, y - 1) + 1



flag = True

while flag == True:

    a = int(input('Введите неотрицательное число A: '))
    b = int(input('Введите неотрицательное число B: '))
    
    if a >= 0 and b >= 0:
        flag = False
    
    else:
        print('\nПопробуйте ещё раз!')

print(summa(a, b))