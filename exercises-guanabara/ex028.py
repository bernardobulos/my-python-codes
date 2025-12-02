# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. 🇧🇷
# Write a program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number the computer chose. The program should then display whether the user won or lost. 🇺🇸
# Escriba un programa que haga que la computadora "piense" en un número entero entre 0 y 5 y pida al usuario que intente adivinar qué número eligió. El programa debería mostrar si el usuario ganó o perdió. 🇪🇸
# Écrivez un programme qui fait « réfléchir » l'ordinateur à un entier compris entre 0 et 5 et qui invite l'utilisateur à deviner le nombre choisi. Le programme doit ensuite afficher si l'utilisateur a gagné ou perdu. 🇫🇷

from random import randint
import time, sys

computer_number = randint(0, 5)

print("GUESSING GAME")
print(" – Hello, player. I'm thinking of a whole number from 0 to 5, try to guess!")

i_guess = int(input("Give your guess: "))

for i in range(12):
    dots = "." * (i % 4)
    sys.stdout.write(f"\rProcessing{dots}   ")
    sys.stdout.flush()
    time.sleep(0.4)

if i_guess == computer_number:
    print(f"\nYOU WON! 😀\nCongratulations, player.")
else:
    print(f"\nYou lost… 😔\nI thought of the number {computer_number}.")
