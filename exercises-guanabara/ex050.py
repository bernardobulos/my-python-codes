# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles valores que forem pares. Se o valor digitado for ímpar, desconsidere-o. 🇧🇷
# Develop a program that reads six integers and displays the sum of only those values ​​that are even. If the entered value is odd, disregard it. 🇺🇸
# Desarrolla un programa que lea seis enteros y muestre solo la suma de los valores pares. Si el valor introducido es impar, ignóralo. 🇪🇸
# Concevez un programme qui lit six entiers et affiche la somme uniquement des nombres pairs. Si la valeur saisie est impaire, ignorez-la. 🇫🇷

sum_num = 0
even_num = 0

for i in range(6):
    num = int(input(f"Enter the {i + 1}º integer: "))
    if num % 2 == 0:
        sum_num += num
        even_num += 1

if even_num == 1:
    print(f"The total sum of the six even integers (given that only {even_num} is the total value entered) is {sum_num}.")
elif even_num == 0:
    print(f"The total sum of the six even integers (with no total value entered) is {sum_num}.")
else:
    print(f"The total sum of the six even integers (where {even_num} is the total number of values ​​entered) is {sum_num}.")
