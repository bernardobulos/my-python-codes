# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 🇧🇷
# Write a program that asks an employee for their salary and calculates the amount of their raise. For salaries above 1,250.00, calculate a 10% raise. For salaries equal to or below this amount, the raise is 15%. 🇺🇸
# Escriba un programa que pregunte a un empleado su salario y calcule el monto de su aumento. Para salarios superiores a 1250,00, calcule un aumento del 10 %. Para salarios iguales o inferiores a esta cantidad, el aumento es del 15 %. 🇪🇸
# Écrivez un programme qui demande le salaire d'un employé et calcule son augmentation. Pour un salaire supérieur à 1 250,00, l'augmentation est de 10 %. Pour un salaire inférieur ou égal à 1 250,00, l'augmentation est de 15 %. 🇫🇷

salario = float(input("Enter an employee's salary: R$ "))

if salario > 1250:
    salario = salario + salario * 0.10
    print(f"This employee received a 10% raise, bringing their current salary to R$ {salario:.2f}.")
else:
    salario = salario + salario * 0.15
    print(f"This employee received a 15% raise, bringing their current salary to R$ {salario:.2f}.")
