# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. 🇧🇷
# Write a program that reads an integer and displays on the screen whether it is EVEN or ODD. 🇺🇸
# Escriba un programa que lea un número entero y muestre en la pantalla si es PAR o IMPAR. 🇪🇸
# Écrivez un programme qui lit un entier et affiche à l'écran s'il est PAIR ou IMPAIR. 🇫🇷

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"The integer {num} is even.")
else:
    print(f"The integer {num} is odd.")
