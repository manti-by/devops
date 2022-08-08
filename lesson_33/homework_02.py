"""
Написать функцию, которая будет вызывать задержку выполнения программы случайным образом от 1-й до 5-ти секунд.
Написать декоратор, который будет выводить на печать время выполнения этой функции (end_time - start_time).
"""

import time
import random
import datetime


def decoration_func(func):
    def wrapper_func():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"Exec time {end_time - start_time}")
    return wrapper_func


@decoration_func
def sleep_func():
    sleep_time = random.randint(1, 3)
    time.sleep(sleep_time)
    print(f"Sleep time in seconds - {sleep_time}")


if __name__ == "__main__":
    for _ in range(5):
        sleep_func()
