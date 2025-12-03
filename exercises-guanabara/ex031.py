# Desenvolva um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem, cobrando R$ 0,50 por quilômetro para viagens de até 200 km e R$ 0,45 para viagens mais longas. 🇧🇷
# Develop a program that asks for the distance of a trip in kilometers. Calculate the fare, charging R$ 0.50 per kilometer for trips up to 200 km and R$ 0.45 for longer trips. 🇺🇸
# Desarrollar un programa que solicite la distancia de un viaje en kilómetros. Calcular la tarifa, cobrando R$ 0,50 por kilómetro para viajes de hasta 200 km y R$ 0,45 para viajes más largos. 🇪🇸
# Concevez un programme qui demande la distance d'un trajet en kilomètres. Calculez le prix de la course : 0,50 R$ par kilomètre pour les trajets jusqu'à 200 km et 0,45 R$ pour les trajets plus longs. 🇫🇷

distance = float(input("Enter the distance of a trip (km): "))

if distance <= 200:
    prix = distance * 0.50
    print(f"The ticket price will be R$ {prix:.2f}.")
else:
    prix = distance * 0.45
    print(f"The ticket price will be R$ {prix:.2f}.")


# ANOTHER WAY TO DO IT
# distance = float(input("Enter the distance of a trip (km): "))
# prix = distance * 0.50 if distance <= 200 else distance * 0.45
# print(f"The ticket price will be R$ {prix:.2f}")
