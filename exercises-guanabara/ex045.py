# Crie um programa que faça o computador jogar "Jokenpô" com você. 🇧🇷
# Create a program that makes the computer play "Rock, Paper, Scissors" with you. 🇺🇸
# Crea un programa que haga que la computadora juegue "Piedra, papel o tijera" contigo. 🇪🇸
# Créez un programme qui permette à l'ordinateur de jouer à « Pierre, Feuille, Ciseaux » avec vous. 🇫🇷

from random import randint
from time import sleep

plays = ["Rock", "Paper", "Scissors"]
computer = randint(0, 2)

print("ROCK, PAPER, SCISSORS")
print("[1] Rock")
print("[2] Paper")
print("[3] Scissors")
play = int(input("Make your move: "))
player = play - 1

print("\nROCK,")
sleep(0.5)
print("PAPER,")
sleep(0.5)
print("SCISSORS!\n")
sleep(0.3)

print(f"The Player chose {plays[player]}.")
print(f"The Computer chose {plays[computer]}.\n")


if computer == 0: # Computer played "Rock"
    if player == 0: # Player played "Rock"
        print("It was a draw! 💥")
    elif player == 1: # Player played "Paper"
        print("The Player won! 🏆")
        print("The Computer lost… 😔")
    elif player == 2: # Player played "Scissors"
        print("The Player lost… 😔")
        print("The Computer won! 🏆")
    else:
        print("\033[31mInvalid play.\033[m")

elif computer == 1: # Computer played "Paper"
    if player == 0: # Player played "Rock"
        print("The Player lost… 😔")
        print("The Computer won! 🏆")
    elif player == 1: # Player played "Paper"
        print("It was a draw! 💥")
    elif player == 2: # Player played ""Scissors"
        print("The Player won! 🏆")
        print("The Computer lost… 😔")
    else:
        print("\033[31mInvalid play.\033[m")

else: # Computer played "Scissors"
    if player == 0: # Player played "Rock"
        print("The Player won! 🏆")
        print("The Computer lost… 😔")
    elif player == 1: # Player played "Paper"
        print("The Player lost… 😔")
        print("The Computer won! 🏆")
    elif player == 2: # Player played "Scissors"
        print("It was a draw! 💥")
    else:
        print("\033[31mInvalid play.\033[m")
