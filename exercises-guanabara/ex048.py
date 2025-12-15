# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500. 🇧🇷
# Write a program that calculates the sum of all odd numbers that are multiples of three and are in the range of 1 to 500. 🇺🇸
# Escriba un programa que calcule la suma de todos los números impares que sean múltiplos de tres y estén en el rango de 1 a 500. 🇪🇸
# Écrivez un programme qui calcule la somme de tous les nombres impairs multiples de trois compris entre 1 et 500. 🇫🇷

sum_num = 0
odd_num = 0
for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            sum_num += num
            odd_num += 1
print(f"The following is the sum of all odd numbers that are multiples of three (with a total of {odd_num} values) in the range from 1 to 500: {sum_num}.")
