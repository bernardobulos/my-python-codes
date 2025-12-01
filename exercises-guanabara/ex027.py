# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Exemplo: Ana Maria de Souza, o primeiro nome será "Ana" e o último "Souza". 🇧🇷
# Write a program that reads a person's full name and then displays the first and last names separately. Example: Ana Maria de Souza, the first name will be "Ana" and the last name "Souza". 🇺🇸
# Escriba un programa que lea el nombre completo de una persona y luego muestre el nombre y el apellido por separado. Ejemplo: Ana María de Souza, el nombre será "Ana" y el apellido "Souza". 🇪🇸
# Écrivez un programme qui lit le nom complet d'une personne et affiche ensuite son prénom et son nom de famille séparément. Exemple : Ana Maria de Souza, le prénom sera « Ana » et le nom de famille « Souza ». 🇫🇷

name = str(input("Enter a person's full name: ")).strip()
separate_names = name.split()

print(f" – This person's first name is {separate_names[0]}.")
print(f" – This person's last name is {separate_names[-1]}.")
