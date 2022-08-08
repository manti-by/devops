"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский,
где слово - это входной параметр, вторая функция - с русского на английский.
"""
import csv


def translate_eng_to_rus(dictionary, word):
    return dictionary.get(word, "Error")


def translate_rus_to_eng(dictionary, word):
    for key, value in dictionary.items():
        if value == word:
            return key
    return "Error"


def get_dictionary(file_name="dictionary.csv"):
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        return {
            row[0]: row[1]
            for row in reader
        }


if __name__ == "__main__":
    dictionary = get_dictionary()

    print(translate_eng_to_rus(dictionary, "color"))
    print(translate_rus_to_eng(dictionary, "ваыпвап"))
