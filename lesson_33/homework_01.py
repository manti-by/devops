"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так, чтобы они не били друг друга
(ферзь может ходить по горизонтали, вертикали и диагонали).
Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


def is_figures_beat_each_other(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


def check_coords(x1: int, y1: int, x2: int, y2: int) -> bool:
    return (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    if is_figures_beat_each_other(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()