class Word:
    """ Класс для слов, определяющий сравнение по длине слов. """

    def __init__(self, word):
        self.word = word

    def __gt__(self, other):
        return len(self.word) > len(other.word)

    def __lt__(self, other):
        return len(self.word) < len(other.word)

    def __ge__(self, other):
        return len(self.word) >= len(other.word)

    def __le__(self, other):
        return len(self.word) <= len(other.word)


if __name__ == "__main__":
    test = Word("test")
    template = Word("template")

    print(test < template)
