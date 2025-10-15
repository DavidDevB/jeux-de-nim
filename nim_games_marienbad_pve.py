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

    """
    Boucle while permettant de prendre des allumettes tant que le compte d'allumettes est supérieur à zéro.
    """
    while sum(matches.values()) > 0:

        """
        Tour du premier joueur
        """
        while True:
            row = input(f"{first_player}, in which row do you pick matches? 1/2/3/4?: ")
            if not row.isdigit() or int(row) < 1 or int(row) > 4 :
                print("Choose between row 1 and 4!")
                continue
            match row:
                case "1":
                    if matches["1"] == 0:
                        print("No matches left!")
                        continue
                    matches["1"] -= 1
                case "2":
                    if matches["2"] == 0:
                        print("No matches left!")
                        continue
                    first_player_play = input("How many matches do you pick? 1/2/3?: ")
                    while int(first_player_play) > 3 or int(first_player_play) < 1:
                        print("You must pick between 1 and 3 matches!")
                        first_player_play = input("How many matches do you pick? ")
                    while int(first_player_play) > matches["2"]:
                        print("Not enough matches!")
                        first_player_play = input("How many matches do you pick? 1/2/3?: ")
                    matches["2"] -= int(first_player_play)
                case "3":
                    if matches["3"] == 0:
                        print("No matches left!")
                        continue
                    first_player_play = input("How many matches do you pick? 1/2/3/4/5?: ")
                    while int(first_player_play) > 5 or int(first_player_play) < 1:
                        print("You must pick between 1 and 3 matches!")
                        first_player_play = input("How many matches do you pick? ")
                    while int(first_player_play) > matches["3"]:
                        print("Not enough matches!")
                        first_player_play = input("How many matches do you pick? 1/2/3/4/5?: ")
                    matches["3"] -= int(first_player_play)
                case "4":
                    if matches["4"] == 0:
                        print("No matches left!")
                        continue
                    first_player_play = input("How many matches do you pick? 1/2/3/4/5/6/7?: ")
                    while int(first_player_play) > 7 or int(first_player_play) < 1:
                        print("You must pick between 1 and 7 matches!")
                        first_player_play = input("How many matches do you pick? ")
                    while int(first_player_play) > matches["4"]:
                        print("Not enough matches!")
                        first_player_play = input("How many matches do you pick? 1/2/3/4/5/6/7?: ")
                    matches["4"] -= int(first_player_play)

            print(f"Matches left: {matches}")
            if sum(matches.values()) <= 0:
                print(f"{second_player} wins!")
                break
            break

        """
        Tour du second joueur
        """
        while True:
            row = input(f"{second_player}, in which row do you pick matches? 1/2/3/4?: ")
            if not row.isdigit() or 1 > int(row) or int(row) > 4:
                print("Choose between row 1 and 4!")
                continue
            match row:
                case "1":
                    if matches["1"] == 0:
                        print("No matches left!")
                        continue
                    matches["1"] -= 1
                case "2":
                    if matches["2"] == 0:
                        print("No matches left!")
                        continue
                    second_player_play = input(f"How many matches do you pick? 1/2/3?: ")
                    while int(second_player_play) > 3 or int(second_player_play) < 1:
                        print("You must pick between 1 and 3 matches!")
                        second_player_play = input(f"How many matches do you pick? ")
                    while int(second_player_play) > matches["2"]:
                        print("Not enough matches!")
                        second_player_play = input(f"How many matches do you pick? 1/2/3?: ")
                    matches["2"] -= int(second_player_play)
                case "3":
                    if matches["3"] == 0:
                        print("No matches left!")
                        continue
                    second_player_play = input(f"How many matches do you pick? 1/2/3/4/5?: ")
                    while int(second_player_play) > 5 or int(second_player_play) < 1:
                        print("You must pick between 1 and 3 matches!")
                        second_player_play = input(f"How many matches do you pick? ")
                    while int(second_player_play) > matches["3"]:
                        print("Not enough matches!")
                        second_player_play = input(f"How many matches do you pick? 1/2/3/4/5?: ")
                    matches["3"] -= int(second_player_play)
                case "4":
                    if matches["4"] == 0:
                        print("No matches left!")
                        continue
                    second_player_play = input(f"How many matches do you pick? 1/2/3/4/5/6/7?: ")
                    while int(second_player_play) > 7 or int(second_player_play) < 1:
                        print("You must pick between 1 and 7 matches!")
                        second_player_play = input(f"How many matches do you pick? ")
                    while int(second_player_play) > matches["4"]:
                        print("Not enough matches!")
                        second_player_play = input(f"How many matches do you pick? 1/2/3/4/5/6/7?: ")
                    matches["4"] -= int(second_player_play)
            print(f"Matches left: {matches}")
            if sum(matches.values()) <= 0:
                print(f"{first_player} wins!")
                break
            break


if __name__ == "__main__":
    play()