"""
Написать функцию, которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random


def get_random_card():
    nom = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    nom_rand = random.choice(nom)

    mas = ["H", "D", "C", "S"]
    mas_rand = random.choice(mas)
    return nom_rand, mas_rand


if __name__ == "__main__":
    nom_rand, mas_rand = get_random_card()
    print(f"Твоя карта: {nom_rand}:{mas_rand}")

    while True:
        choice = input("Достать ещё одну карту?")
        if choice == "Y":
            nom_rand, mas_rand = get_random_card()
            print(f"{nom_rand}:{mas_rand}")
        else:
            break

    print("Game over.")
