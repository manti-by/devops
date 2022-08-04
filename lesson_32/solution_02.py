"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и
возвращает их сумму и максимальное из них.
"""


def sum_and_max(*args):
    my_sum = 0
    my_max = args[0]
    for x in args:
        my_sum += x
        if x > my_max:
            my_max = x
    return my_sum, my_max
