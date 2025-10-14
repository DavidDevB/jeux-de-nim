#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


"""Récupère et retourne le nom d'utilisateur"""
def get_user_name():
    return input("Enter you username: ")


"""Les noms des joueurs sont mis dans une liste pour pouvoir être choisis au hasard ensuite"""
player1 = get_user_name()
player2 = get_user_name()
players = [player1, player2]


"""Définie le joueur qui commence"""
def get_first_player():
    return random.choice([player1, player2])


"""Fonction principale de fonctionnement du jeu"""
def play():

    print("Welcome to Nim's game!")
    print("...Loading")
    for _ in range(5):
        print("...")

    first_player = get_first_player()
    second_player = players[1] if first_player == players[0] else players[0]

    matches = 21

    print(f"{first_player} plays first!")

    print("Start!")

    # Boucle while permettant de prendre des allumettes tant que le compte d'allumettes est supérieur à zéro.
    while matches > 0:
        while True:
            first_player_play = input(f"{first_player}, how many matches do you pick? ")
            if int(first_player_play) > 4 or int(first_player_play) < 1:
                print("You must pick between 1 and 4 matches!")
                first_player_play = input(f"{first_player}, how many matches do you pick? ")
            if int(first_player_play) > matches:
                print("Not enough matches left!")
                first_player_play = input(f"{second_player}, how many matches do you pick? ")
            matches -= int(first_player_play)
            print(f"Matches left: {matches}")
            if matches <= 0:
                print(f"{second_player} wins!")
                break
            break

        while True:
            second_player_play = input(f"{second_player}, how many matches do you pick? ")
            if int(second_player_play) > 4 or int(second_player_play) < 1:
                print("You must pick between 1 and 4 matches!")
                second_player_play = input(f"{second_player}, how many matches do you pick? ")
            if int(second_player_play) > matches:
                print("Not enough matches left!")
                second_player_play = input(f"{second_player}, how many matches do you pick? ")
            matches-= int(second_player_play)
            print(f"Matches left: {matches}")
            if matches <= 0:
                print(f"{first_player} wins!")
                break
            break
    print("Game over!")

if __name__ == "__main__":
    play()