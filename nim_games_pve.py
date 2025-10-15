#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux de Nim (et variante de Marienbad)
"""


"""
Récupère et retourne le nom d'utilisateur
"""
def get_user_name():
    while True:
        username = input("Enter you username: ")
        if username.strip().lower() == "comp":
            print("'Comp' is reserved for the computer. Please choose another name.")
            continue
        return username


"""
Définie le joueur qui commence
"""
def get_first_player(player):
    return input(f"Who starts ? Comp/{player} ?: ")


"""
Fonction principale de fonctionnement du jeu
"""
def play():

    print("Welcome to Nim's game!")
    print("...Loading")
    for _ in range(5):
        print("...")

    player = get_user_name()
    comp = "Computer"

    starter = get_first_player(player).lower()

    first_player = ""

    match starter:
        case "comp":
            first_player = comp
        case _ if starter == player:
            first_player = player

    matches = 21

    print(first_player)
    print(f"{first_player} plays first!")

    print("Start!")

    """
    Boucle while permettant de prendre des allumettes tant que le compte d'allumettes est supérieur à zéro.
    """
    while matches > 0:
        if matches == 21 and first_player == "Computer":
            matches -= 4
            print("Computer picked 4 matches!")
            print(f"Matches left: {matches}")
        while True:
            player_play = input(f"{player}, how many matches do you pick? ")
            if int(player_play) > 4 or int(player_play) < 1:
                print("You must pick between 1 and 4 matches!")
                player_play = input(f"{player}, how many matches do you pick? ")
            if int(player_play) > matches:
                print("Not enough matches left!")
                player_play = input(f"{player}, how many matches do you pick? ")
            matches -= int(player_play)
            print(f"Matches left: {matches}")
            if matches <= 0:
                print(f"{comp} wins!")
                print("Game over!")
                break
            print(f"Computer picked {5 - int(player_play)} matches!")
            matches -= (5 - int(player_play))
            print(f"Matches left: {matches}")
            if matches <= 0:
                print(f"{player} wins!")
                print("Game over!")
                break
            break


if __name__ == "__main__":
    play()