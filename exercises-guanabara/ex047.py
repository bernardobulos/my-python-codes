# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 🇧🇷
# Write a program that displays on the screen all the even numbers that are in the range between 1 and 50. 🇺🇸
# Escriba un programa que muestre en la pantalla todos los números pares que estén en el rango entre 1 y 50. 🇪🇸
# Écrivez un programme qui affiche à l'écran tous les nombres pairs compris entre 1 et 50. 🇫🇷

print("Below are all the even numbers in the range from 1 to 50: ", end="")
for num in range(1, 51):
    if num % 2 == 0:
        if num == 50:
            print(num, end=".")
        else:
            print(num, end=", ")
