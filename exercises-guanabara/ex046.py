# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. 🇧🇷
# Write a program that displays a countdown on the screen for a fireworks display, going from 10 to 0, with a 1-second pause between each countdown. 🇺🇸
# Escriba un programa que muestre una cuenta regresiva en la pantalla para un espectáculo de fuegos artificiales, que vaya de 10 a 0, con una pausa de 1 segundo entre cada cuenta regresiva. 🇪🇸
# Écrivez un programme qui affiche un compte à rebours à l'écran pour un feu d'artifice, allant de 10 à 0, avec une pause d'une seconde entre chaque décompte. 🇫🇷

from time import sleep
from datetime import date

data = date.today().year
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print("HAPPY NEW YEAR!")
print(f"May the year {data + 1} be incredible!")
