# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa. 🇧🇷
# Write a program that reads the lengths of the opposite and adjacent sides of a triangle, calculates and displays the length of the hypotenuse. 🇺🇸
# Escribe un programa que lea las longitudes de los lados opuesto y adyacente de un triángulo, calcule y muestre la longitud de la hipotenusa. 🇪🇸
# Écrivez un programme qui lit les longueurs des côtés opposés et adjacents d'un triangle, calcule et affiche la longueur de l'hypoténuse. 🇫🇷

from math import hypot

cat_oposto = float(input("Enter the opposite side of a triangle: "))
cat_adjacente = float(input("Enter the adjacent side of a triangle: "))

hip = hypot(cat_oposto, cat_adjacente)

print(f"The length of the hypotenuse of this triangle is {hip:.2f}.")
