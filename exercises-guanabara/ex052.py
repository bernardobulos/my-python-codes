# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 🇧🇷
# Write a program that reads an integer and determines whether or not it is a prime number. 🇺🇸
# Escriba un programa que lea un número entero y determine si es o no un número primo. 🇪🇸
# Écrivez un programme qui lit un entier et détermine s'il s'agit ou non d'un nombre premier. 🇫🇷

num = int(input("Enter an integer: "))

if num <= 1:
    print(f"The number {num} is not prime.")
else:
    div_num = 0
    for i in range(1, num + 1):
        if num % i == 0:
            print(f"\033[33m{i}\033[m", end=" → ")
            div_num += 1
        else:
            print(f"\033[31m{i}\033[m", end=" → ")
    print("\033[32mEND\033[m.")

    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        print(f"\nThe number {num} was divisible by 2 times.")
        print(f"Therefore, it is a cousin.")
    else:
        print(f"\nThe number {num} was divisible {div_num} times.")
        print(f"Therefore, it is not a cousin.")
