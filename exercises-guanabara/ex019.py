# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 🇧🇷
# A teacher wants to randomly select one of his four students to erase the board. Write a program to help him by reading their names and writing the name of the chosen student. 🇺🇸
# Un profesor quiere elegir al azar a uno de sus cuatro alumnos para que borre la pizarra. Escribe un programa que le ayude leyendo sus nombres y escribiendo el nombre del alumno elegido. 🇪🇸
# Un professeur souhaite choisir au hasard un de ses quatre élèves pour effacer le tableau. Écrivez un programme qui l'aide en lisant les noms des élèves et en affichant celui de l'élève choisi. 🇫🇷

from random import choice

nome1 = str(input("Enter the name of the 1st student: "))
nome2 = str(input("Enter the name of the 2nd student: "))
nome3 = str(input("Enter the name of the 3rd student: "))
nome4 = str(input("Enter the name of the 4th student: "))

lista_nomes = [nome1, nome2, nome3, nome4]
escolhido = choice(lista_nomes)

print(f"The student chosen was {escolhido}.")
