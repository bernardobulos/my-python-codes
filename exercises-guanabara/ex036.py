# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. 🇧🇷
# Write a program to approve a bank loan for the purchase of a house. Ask for the house value, the buyer's salary, and the repayment period. The monthly payment cannot exceed 30% of the salary, otherwise the loan will be denied. 🇺🇸
# Redacte un programa para aprobar un préstamo bancario para la compra de una vivienda. Solicite el valor de la vivienda, el salario del comprador y el plazo de amortización. El pago mensual no puede superar el 30% del salario; de lo contrario, el préstamo será denegado. 🇪🇸
# Écrivez un programme permettant d'approuver une demande de prêt bancaire pour l'achat d'une maison. Le programme doit demander la valeur du bien, le salaire de l'emprunteur et la durée du remboursement. Le montant des mensualités ne doit pas dépasser 30 % du salaire, sous peine de refus du prêt. 🇫🇷

house_value = float(input("Enter the house value: R$ "))
buyers_salary = float(input("Enter the buyer's salary: R$ "))
years_payment = int(input("Enter the number of years the buyer will pay: "))

max_payment_allowed = buyers_salary * 0.30
monthly_payment = house_value / (years_payment * 12)

if years_payment > 1:
    print(f"The monthly payment is R$ {monthly_payment:.2f} to pay for a house worth R$ {house_value:.2f} in {years_payment} years.")
else:
    print(f"The monthly payment is R$ {monthly_payment:.2f} to pay for a house worth R$ {house_value:.2f} in {years_payment} year.")

if monthly_payment <= max_payment_allowed:
    print("The loan may be granted.")
else:
    print("The loan is denied.")
