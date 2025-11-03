# Crie um programa que leia quanto dinheiro (em reais) uma pessoa tem na carteira e mostre quantos dólares americanos, dólares canadenses, euros e ienes ela pode comprar (10 de outubro de 2025). 🇧🇷
# Write a program that reads how much money (in reais) a person has in their wallet and shows how many US dollars, Canadian dollars, euros, and yen they can buy (October 10, 2025). 🇺🇸
# Escriba un programa que lea la cantidad de dinero (en reales) que una persona tiene en su billetera y muestre cuántos dólares estadounidenses, dólares canadienses, euros y yenes puede comprar (10 de octubre de 2025). 🇪🇸
# Écrivez un programme qui lit le montant d'argent (en reais) qu'une personne possède dans son portefeuille et affiche le nombre de dollars américains, de dollars canadiens, d'euros et de yens qu'elle peut acheter (10 octobre 2025). 🇫🇷

real = float(input("Enter your total wallet balance (in Brazilian Reais): R$ "))
print(f" — You can buy {real / 5.31:.2f} dollars (United States).")
print(f" — You can buy {real / 3.81:.2f} dollars (Canada).")
print(f" — You can buy {real / 6.22:.2f} euros (Europe).")
print(f" — You can buy {real / 0.04:.2f} yen (Japan).")
