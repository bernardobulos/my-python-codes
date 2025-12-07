# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista (dinheiro/cheque) = 10% de desconto; à vista no cartão = 5% de desconto; em até 2 vezes no cartão = preço normal; e 3 vezes ou mais no cartão = 20% de juros. 🇧🇷
# Write a program that calculates the amount to be paid for a product, considering its regular price and payment terms: cash (money/check) = 10% discount; card payment = 5% discount; up to 2 installments by card = regular price; and 3 or more installments by card = 20% interest. 🇺🇸
# Escriba un programa que calcule el monto a pagar por un producto, considerando su precio regular y condiciones de pago: efectivo (dinero/cheque) = 10% de descuento; pago con tarjeta = 5% de descuento; hasta 2 cuotas con tarjeta = precio regular; y 3 o más cuotas con tarjeta = 20% de interés. 🇪🇸
# Écrivez un programme qui calcule le montant à payer pour un produit, en tenant compte de son prix normal et de ses modalités de paiement : espèces (argent/chèque) = 10 % de réduction ; paiement par carte = 5 % de réduction ; jusqu’à 2 versements par carte = prix normal ; et 3 versements ou plus par carte = 20 % d’intérêt. 🇫🇷

price = float(input("Enter the price of a product: R$ "))

print("""WHAT ARE THE PAYMENT TERMS?
 • Enter \"1\" to pay cash/check.
    — 10% discount.
 • Enter \"2\" to pay card. 
    — 5% discount.
 • Enter \"3\" to pay in 2 installments by card.
    — Regular price.
 • Enter \"4\" to pay in 3 or more installments by card.
    — 20% simple interest.""")
option = int(input("Enter your option: "))

match option:
    case 1:
        discount10 = price - (price * 0.10)
        print(f"The final product price will be R$ {discount10:.2f}, with a 10% discount.")
    case 2:
        discount5 = price - (price * 0.05)
        print(f"The final product price will be R$ {discount5:.2f}, with a 5% discount.")
    case 3:
        halfprice = price / 2
        print(f"The final product price will be R$ {price:.2f}, divided into 2 installments of R$ {halfprice}.")
    case 4:
        inst = int(input("Please specify the number of installments: "))
        interest_rate = price + (price * 0.20)
        instprice = interest_rate / inst
        print(f"The final product price will be R$ {interest_rate:.2f}, with 20% simple interest, divided into {inst} installments of R$ {instprice:.2f}.")
    case _:
        print("\033[31mInvalid payment condition.\033[m")
