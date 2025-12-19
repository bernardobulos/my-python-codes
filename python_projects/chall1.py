# Você foi contratado para desenvolver um programa simples que auxilie no processo de compra de um produto. O programa deve permitir que o usuário insira o nome e o preço de vários produtos, perguntando se ele deseja continuar adicionando mais produtos após cada entrada. Ao final, o programa deve fornecer um resumo da compra, incluindo: o total gasto, o número de produtos que custam mais de US$ 200 e o nome do produto mais barato. Desenvolva o programa em Python utilizando conceitos de entrada/saída de dados, condicionais e laços de repetição. 🇧🇷
# You have been hired to develop a simple program to assist in a product purchase process. The program should allow the user to enter the name and price of several products, asking if they wish to continue entering more products after each entry. At the end, the program should provide a summary of the purchase, including: the total spent, the number of products costing more than US$200, and the name of the cheapest product. Develop the program in Python using concepts of data input/output, conditionals, and loops. 🇺🇸
# Se le ha contratado para desarrollar un programa sencillo que facilite el proceso de compra de un producto. El programa debe permitir al usuario introducir el nombre y el precio de varios productos, preguntando si desea introducir más después de cada entrada. Al final, el programa debe proporcionar un resumen de la compra, que incluya: el total gastado, la cantidad de productos con un precio superior a US$200 y el nombre del producto más económico. Desarrolle el programa en Python utilizando conceptos de entrada/salida de datos, condicionales y bucles. 🇪🇸
# Vous avez été engagé(e) pour développer un programme simple d'assistance à l'achat de produits. Ce programme doit permettre à l'utilisateur de saisir le nom et le prix de plusieurs produits, et lui demander s'il souhaite en ajouter d'autres après chaque saisie. À la fin, le programme doit fournir un récapitulatif de l'achat, incluant : le total dépensé, le nombre de produits coûtant plus de 200 $US et le nom du produit le moins cher. Développez ce programme en Python en utilisant les concepts d'entrée/sortie de données, de conditions et de boucles. 🇫🇷

total_expenditure = 0
expensive_products = 0
cheapest_price = 0
cheapest_product = ""

print("\033[1m\nPRODUCT PURCHASE MANAGEMENT [V1.0]\033[m")
while True:
    product_name = str(input("\nEnter the product name: ")).strip()
    product_price = float(input("Enter the product price: US$"))

    total_expenditure += product_price
    if product_price > 1000.00:
        expensive_products += 1
    if cheapest_price == 0 or product_price < cheapest_price:
        cheapest_price = product_price
        cheapest_product = product_name

    print("\nDo you want to add more products?")
    option = str(input("Enter your option [yes/no]: ")).strip().lower()[0]
    if option == "y":
        continue
    elif option == "n":
        break
    else:
        print("\033[3;31mInvalid option.\033[m")
        continue

print(f"\nThe total cost of the purchase was US${total_expenditure:.2f}.")
print(f"The number of products that cost more than US$200 is equal to {expensive_products}.")
print(f"The name of the cheapest product is \"{cheapest_product}\" (for US${cheapest_price:.2f}).\n")
