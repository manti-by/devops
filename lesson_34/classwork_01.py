"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут
имени у объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.

Создать новый класс Cat, который имеет все те же атрибуты, что и Dog,
только заменить метод bark на meow.

Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.
"""
from typing import Optional


class Animal:
    types = ("t2.micro", "t2.small")

    def __init__(self, name, height=None, weight=None, age=None, server_type="x3.micro"):
        self.create(server_type)
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def create(self, server_type):
        if server_type in self.types:
            print("Create server")
        else:
            raise Exception("Server type error")

    def change_name(self, new_name):
        self.name = new_name
        raise BaseException

    def voice(self) -> dict:
        raise NotImplementedError


class Dog(Animal):

    def voice(self):
        print(f"{self.name} barking")
        try:
            self.change_name("Test")
        except BaseException:
            pass


class Cat(Animal):

    def voice(self):
        print(f"{self.name} meowing")


if __name__ == "__main__":
    dog = Dog("Dog")
    dog.voice()

    cat_1 = Cat("Cat")
    cat_1.change_name("New Cat")
    cat_1.voice()

