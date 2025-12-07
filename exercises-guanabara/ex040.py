# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0 = Reprovado, Média entre 5.0 e 6.9 = Recuperação e Média 7.0 ou superior = Aprovado. 🇧🇷
# Write a program that reads two grades from a student and calculates their average, displaying a message at the end according to the average achieved: Average below 5.0 = Failed, Average between 5.0 and 6.9 = Remedial, and Average 7.0 or higher = Passed. 🇺🇸
# Escriba un programa que lea dos calificaciones de un estudiante y calcule su promedio, mostrando un mensaje al final de acuerdo al promedio obtenido: Promedio menor a 5.0 = Reprobado, Promedio entre 5.0 y 6.9 = Remediable, y Promedio 7.0 o mayor = Aprobado. 🇪🇸
# Écrivez un programme qui lit deux notes d'un élève et calcule leur moyenne, en affichant un message à la fin en fonction de la moyenne obtenue : Moyenne inférieure à 5,0 = Échec, Moyenne entre 5,0 et 6,9 = Soutien, et Moyenne de 7,0 ou plus = Réussite. 🇫🇷

grade1 = float(input("Enter a student's first grade (from 0.0 to 10.0): "))
grade2 = float(input("Enter a student's second grade (from 0.0 to 10.0): "))

avarage = (grade1 + grade2) / 2

if avarage < 5.0:
    print(f"This student's average grade was {avarage:.1f}, with corresponding grades of {grade1:.1f} and {grade2:.1f}.")
    print("The student has \033[31mfailed\033[m.")
elif 7.0 > avarage >= 5.0:
    print(f"This student's average grade was {avarage:.1f}, with corresponding grades of {grade1:.1f} and {grade2:.1f}.")
    print("The student is in \033[33mremedial classes\033[m.")
else:
    print(f"This student's average grade was {avarage:.1f}, with corresponding grades of {grade1:.1f} and {grade2:.1f}.")
    print("The student has \033[32mpassed\033[m.")
