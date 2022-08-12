"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3.
На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра.
Диски можно перекладывать с одного стержня на другой строго по одному, при этом диск нельзя класть на
диск меньшего диаметра.

Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний,
необходимую для решения головоломки.
"""


def hanoi_tower_recursive(n, source: int = 0, target: int = 2):
    if n > 0:
        buffer = 3 - source - target
        hanoi_tower_recursive(n - 1, source, buffer)
        print("Перемещаем диск", chr(64 + n), source + 1, "->", target + 1)
        hanoi_tower_recursive(n - 1, buffer, target)


if __name__ == "__main__":
    hanoi_tower_recursive(4)

    # x1 = [1, 2, 3, 4]
    # x2 = []
    # x3 = []
    #
    # while not (len(x2) == 4 or len(x3) == 4):
    #     if not x2 or (x1 and x1[0] < x2[0]):
    #         x2.append(x1.pop(0))
    #         print("1 -> 2")
    #         continue
    #
    #     if not x3 or (x1 and x1[0] < x3[0]):
    #         x3.append(x1.pop(0))
    #         print("1 -> 3")
    #         continue
    #
    #     if not x3 or (x2 and x2[0] < x3[0]):
    #         x3.append(x2.pop(0))
    #         print("2 -> 3")
    #         continue
    #
    #     if not x1 or (x3 and x3[0] < x1[0]):
    #         x1.append(x3.pop(0))
    #         print("3 -> 1")
    #         continue
    #
    #     if not x2 or (x3 and x3[0] < x2[0]):
    #         x2.append(x3.pop(0))
    #         print("3 -> 2")
    #         continue
    #
    # print(f"x1: {x1}")
    # print(f"x2: {x2}")
    # print(f"x3: {x3}")
