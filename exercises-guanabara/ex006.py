# Crie um algoritmo que leia um número e mostre o sue dobro, triplo e raiz quadrada. 🇧🇷
# Create an algorithm that reads a number and displays its double, triple, and square root. 🇺🇸
# Crea un algoritmo que lea un número y muestre su doble, triple y raíz cuadrada. 🇪🇸
# Créez un algorithme qui lit un nombre et affiche sa racine double, sa racine triple et sa racine carrée. 🇫🇷

from math import sqrt

n = int(input("Enter an integer: "))
print(f"The double the number {n} is {n*2}.")
print(f"The triple the number {n} is {n*3}.")
print(f"The square root of the number {n} is {sqrt(n):.2f}.")
