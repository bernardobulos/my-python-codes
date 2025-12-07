# Faça um programa que leia três números inteiros e mostre qual é o maior e qual é o menor. 🇧🇷
# Write a program that reads three integers and displays which is the largest and which is the smallest. 🇺🇸
# Escriba un programa que lea tres números enteros y muestre cuál es el más grande y cuál es el más pequeño. 🇪🇸
# Écrivez un programme qui lit trois entiers et affiche lequel est le plus grand et lequel est le plus petit. 🇫🇷

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 > n2 and n1 > n3:
    print(f"The number {n1} is greater.")
    if n2 > n3:
        print(f"The number {n3} is smaller.")
    else:
        print(f"The number {n2} is smaller.")
elif n2 > n1 and n2 > n3:
    print(f"The number {n2} is greater.")
    if n1 > n3:
        print(f"The number {n3} is smaller.")
    else:
        print(f"The number {n1} is smaller.")
else:
    print(f"The number {n3} is greater.")
    if n1 > n2:
        print(f"The number {n2} is smaller.")
    else:
        print(f"The number {n1} is smaller.")
