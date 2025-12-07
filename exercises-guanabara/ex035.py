# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. 🇧🇷
# Develop a program that reads the lengths of three lines and tells the user whether or not they can form a triangle. 🇺🇸
# Desarrollar un programa que lea la longitud de tres líneas y le diga al usuario si pueden o no formar un triángulo. 🇪🇸
# Concevez un programme qui lit les longueurs de trois lignes et indique à l'utilisateur si elles peuvent ou non former un triangle. 🇫🇷

print("CONDITION FOR THE EXISTENCE OF A TRIANGLE")
a = float(input("Type the first line of a triangle: "))
b = float(input("Type the second line of a triangle: "))
c = float(input("Type the third line of a triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The lengths of the three lines can form a triangle.")
else:
    print("The lengths of the three lines cannot form a triangle.")
