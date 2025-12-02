# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada quilômetro acima do limite. 🇧🇷
# Write a program that reads a car's speed. If it exceeds 80 km/h, display a message saying that a fine has been issued. The fine will cost R$7.00 for each kilometer above the speed limit. 🇺🇸
# Écrivez un programme qui lit la vitesse d'une voiture. Si elle dépasse 80 km/h, affichez un message indiquant qu'une amende a été émise. L'amende s'élève à 7,00 R$ par kilomètre au-dessus de la limite de vitesse. 🇫🇷
# Escriba un programa que lea la velocidad de un coche. Si supera los 80 km/h, muestre un mensaje indicando que se ha impuesto una multa. La multa costará R$7,00 por cada kilómetro que exceda el límite de velocidad. 🇪🇸

km_rodado = float(input("Enter the speed of a car: "))
if km_rodado > 80:
    multa = 7 * (km_rodado - 80)
    print(f"This car has been fined for exceeding {km_rodado:.2f} km/h.\nPay R$ {multa:.2f}.")
else:
    print("This car is within the limits.")
