# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 🇧🇷
# Write a program that reads a person's name and tells them if "SILVA" is in their name. 🇺🇸
# Escriba un programa que lea el nombre de una persona y le diga si "SILVA" está en su nombre. 🇪🇸
# Écrivez un programme qui lit le nom d'une personne et lui indique si le nom contient « SILVA ». 🇫🇷

name = str(input("Enter a person's name: ")).strip()

if "SILVA" in name.upper():
    print(f"The name {name} has \"SILVA\".")
else:
    print(f"The name {name} does not have \"SILVA\".")
