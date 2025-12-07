# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: "o primeiro valor é maior", "o segundo valor é maior" ou "não existe valor maior, os dois são iguais". 🇧🇷
# Write a program that reads two integers and compares them, displaying the message "the first value is greater", "the second value is greater" or "there is no greater value, they are equal". 🇺🇸
# Escriba un programa que lea dos números enteros y los compare, mostrando el mensaje "el primer valor es mayor", "el segundo valor es mayor" o "no hay valor mayor, son iguales". 🇪🇸
# Écrivez un programme qui lit deux entiers et les compare, en affichant le message « la première valeur est supérieure », « la deuxième valeur est supérieure » ou « il n'y a pas de valeur supérieure, elles sont égales ». 🇫🇷

n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))

if n1 > n2:
    print(f"The number {n1} is greater.")
elif n2 > n1:
    print(f"The number {n2} is greater.")
else:
    print("Both numbers are equal.")
