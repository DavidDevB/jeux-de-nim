#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeux de Nim (et variante de Marienbad)
"""


import random


"""
Récupère et retourne le nom d'utilisateur
"""
def get_user_name():
    return input("Enter you username: ")


"""
Les noms des joueurs sont mis dans une liste pour pouvoir être choisis au hasard ensuite
"""
player1 = get_user_name()
player2 = get_user_name()
players = [player1, player2]


"""
Définie le joueur qui commence
"""
def get_first_player():
    return random.choice([player1, player2])


"""
Fonction principale de fonctionnement du jeu
"""
def play():

    print("Welcome to Nim's game!")
    print("...Loading")
    for _ in range(5):
        print("...")

    first_player = get_first_player()
    second_player = players[1] if first_player == players[0] else players[0]

    matches = {"1": 1, "2": 3, "3": 5, "4": 7}

    print(f"{first_player} plays first!")

    print("Start!")
    print(matches)

    """
    Boucle while permettant de prendre des allumettes tant que le compte d'allumettes est supérieur à zéro.
    """
    while sum(matches.values()) > 0:

        """
        Tour du premier joueur
        """
        while True:
            row = input(f"{first_player}, in which row do you pick matches? 1/2/3/4?: ")
            if not row.isdigit() or int(row) < 1 or int(row) > 4:
                print("Choose between row 1 and 4!")
                continue
            max_pick = matches[row]
            if max_pick == 0:
                print("No matches left in this pile!")
                continue
            try:
                pick = int(input(f"How many matches do you pick (1 to {max_pick})? "))
            except ValueError:
                print("Enter a valid number.")
                continue

            if not (1 <= pick <= max_pick):
                print("Invalid number of matches.")
                continue

            matches[row] -= pick
            print(f"Matches left: {matches}")
            break

        if sum(matches.values()) <= 0:
            print(f"{second_player} wins!")
            break

        """
        Tour du second joueur
        """
        while True:
            row = input(f"{second_player}, in which row do you pick matches? 1/2/3/4?: ")
            if not row.isdigit() or int(row) < 1 or int(row) > 4:
                print("Choose between row 1 and 4!")
                continue
            max_pick = matches[row]
            if max_pick == 0:
                print("No matches left in this pile!")
                continue
            try:
                pick = int(input(f"How many matches do you pick (1 to {max_pick})? "))
            except ValueError:
                print("Enter a valid number.")
                continue

            if not (1 <= pick <= max_pick):
                print("Invalid number of matches.")
                continue

            matches[row] -= pick
            print(f"Matches left: {matches}")
            break

        if sum(matches.values()) <= 0:
            print(f"{first_player} wins!")
            break



if __name__ == "__main__":
    play()