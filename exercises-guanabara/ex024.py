# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". 🇧🇷
# Create a program that reads the name of a city and tells whether it begins with the name "SANTO". 🇺🇸
# Crea un programa que lea el nombre de una ciudad y diga si comienza o no con el nombre "SANTO". 🇪🇸
# Crée un programme qui lit le nom d’une ville et dit si elle commence ou non par le nom « SANTO ». 🇫🇷

city = str(input("Enter the name of a city: ")).strip()
if city[:5].upper() == "SANTO":
    print(f"The city {city} begins with \"SANTO\".")
else:
    print(f"The city {city} does not begin with \"SANTO\".")
