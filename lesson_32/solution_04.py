"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца -
и возвращает название сезона, к которому относится этот месяц. Например, передаем 2,
на выходе получаем "Winter".
"""


def month_to_season_1(month: int) -> str:
    if 2 < month < 6:
        return "Spring"
    if 5 < month < 9:
        return "Summer"
    if 9 < month < 12:
        return "Autumn"
    return "Winter"


def month_to_season_2(month: int) -> str:
    month_to_season_map = {
        "Winter": [1, 2, 12],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11],
    }
    for season, months in month_to_season_map.items():
        if month in months:
            return season
    return "Not found"
