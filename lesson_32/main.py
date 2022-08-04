import random

from lesson_32.solution_01 import format_name
from lesson_32.solution_02 import sum_and_max
from lesson_32.solution_03 import min_or_max
from lesson_32.solution_04 import month_to_season_1, month_to_season_2

if __name__ == "__main__":
    my_list = [random.randint(1, 100) for _ in range(10)]
    print("Call min", min_or_max(*my_list, func_type="min"))
    print("Call max", min_or_max(*my_list, func_type="max"))

    month = int(input("Enter month number:"))
    print("M2S v1", month_to_season_1(month))
    print("M2S v2", month_to_season_2(month))

    months = input("Enter list:").split(",")
    print(months)
