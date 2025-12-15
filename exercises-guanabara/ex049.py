# Refaça o ex009.py, mostrando a tabuada de um número que o usuário escolher, só que utilizando um laço de repetição (for). 🇧🇷
# Rewrite ex009.py, displaying the multiplication table of a number chosen by the user, but using a for loop. 🇺🇸
# Reescribe ex009.py, mostrando la tabla de multiplicación de un número elegido por el usuario, pero utilizando un bucle for. 🇪🇸
# Réécrivez ex009.py, en affichant la table de multiplication d'un nombre choisi par l'utilisateur, mais en utilisant une boucle for. 🇫🇷

num = int(input("Enter an integer: "))
print(f"MULTIPLICATION TABLE OF NUMBER {num}")
print("-" * 13)
for mult in range(0, 11):
    print(f"{num} × {mult:2} = {num * mult}")
print("-" * 13)
