"""
Написать функцию принимающая на вход неопределенным количеством аргументов и
именованный аргумент func_type.

В зависимости от func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""


def my_min(*args):
    result = args[0]
    for x in args:
        if x < result:
            result = x
    return result


def my_max(*args):
    result = args[0]
    for x in args:
        if x > result:
            result = x
    return result


def min_or_max(*args, **kwargs):
    if kwargs["func_type"] == "min":
        return my_min(*args)
    return my_max(*args)


