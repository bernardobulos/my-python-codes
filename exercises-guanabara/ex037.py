# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal ou 3 para hexadecimal. 🇧🇷
# Write a program that reads any integer and asks the user to choose the conversion base: 1 for binary, 2 for octal, or 3 for hexadecimal. 🇺🇸
# Escriba un programa que lea cualquier número entero y solicite al usuario que elija la base de conversión: 1 para binario, 2 para octal o 3 para hexadecimal. 🇪🇸
# Écrivez un programme qui lit n'importe quel entier et demande à l'utilisateur de choisir la base de conversion : 1 pour le binaire, 2 pour l'octal ou 3 pour l'hexadécimal. 🇫🇷

num = int(input("Enter an integer: "))
print("[1] Binary\n[2] Octal\n[3] Hexadecimal")
option = int(input("Enter your conversion option: "))

match option:
    case 1:
        print("\nBINARY: ", end="")
        print(bin(num)[2:])
    case 2:
        print("\nOCTAL: ", end="")
        print(oct(num)[2:])
    case 3:
        print("\nHEXADECIMAL: ", end="")
        print(hex(num)[2:])
    case _:
        print("Invalid conversion option, please try again.")
