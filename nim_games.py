#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_user_name():
    return input("Enter you username: ")


player1 = get_user_name()
player2 = get_user_name()
players = [player1, player2]


def get_first_player(play1, play2):
    return random.choice([player1, player2])


def play():

    print("Welcome to Nim's game!")
    print("...Loading")
    for _ in range(5):
        print("...")

    first_player = get_first_player(player1, player2)
    second_player = players[1] if first_player == players[0] else players[0]

    matches1 = {first_player: 21}
    matches2 = {second_player: 21}

    print(f"{first_player} plays first!")

    print("Start!")

    while matches1[first_player] | matches2[second_player] > 0:
        first_player_play = input(f"{first_player}, how many matches do you pick? ")
        while int(first_player_play) > 4 or int(first_player_play) < 1:
            print("You must pick between 1 and 4 matches!")
            first_player_play = input(f"{first_player}, how many matches do you pick? ")
        matches1[first_player]  -= int(first_player_play)
        matches2[second_player] -= int(first_player_play)
        print(matches1[first_player])
        if matches1[first_player] <= 0:
            print(f"{player2} wins!")
            break
        second_player_play = input(f"{second_player}, how many matches do you pick? ")
        while int(second_player_play) > 4 or int(second_player_play) < 1:
            print("You must pick between 1 and 4 matches!")
            second_player_play = input(f"{second_player}, how many matches do you pick? ")
        matches2[second_player] -= int(second_player_play)
        matches1[first_player] -= int(second_player_play)
        print(matches1[first_player])
        if matches2[second_player] <= 0:
            print(f"{player1} wins!")
            break
    return None



if __name__ == "__main__":
    play()