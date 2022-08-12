"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости).
"""


class Car:

    color_types = ("green", "red")

    def __init__(self, make: str, model: str, year: int, color: str, speed: int = 0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.color = color

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.speed *= -1

    @property
    def get_speed(self):
        return self.speed


def main():
    print(Car.color_types)

    car = Car("Mercedes", "E500", 2000, Car.color_types[0])
    while car.speed < 100:
        car.increase_speed()
    print("Done!")


if __name__ == "__main__":
    main()
