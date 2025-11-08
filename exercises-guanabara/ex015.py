# Escreva um programa que pergunte a quantidade de quilômetros (km) percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por quilômetro (km) rodado. 🇧🇷
# Write a program that asks for the number of kilometers (km) traveled by a rental car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$ 60 per day and R$ 0.15 per kilometer (km) driven. 🇺🇸
# Escribe un programa que solicite el número de kilómetros (km) recorridos por un coche de alquiler y el número de días de alquiler. Calcula el precio a pagar, sabiendo que el coche cuesta R$ 60 por día y R$ 0,15 por kilómetro (km) recorrido. 🇪🇸
# Écrivez un programme qui demande le nombre de kilomètres parcourus par une voiture de location et le nombre de jours de location. Calculez le prix à payer, sachant que la voiture coûte 60 R$ par jour et 0,15 R$ par kilomètre parcouru. 🇫🇷

km = float(input("Enter the number of kilometers (km) traveled by the rental car: "))
dias = int(input("Enter the number of days the car was rented: "))
pagamento = 60 * dias + 0.15 * km
print(f"The total payment for the rental car will be R$ {pagamento:.2f}.")
