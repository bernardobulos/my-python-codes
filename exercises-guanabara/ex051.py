# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 🇧🇷
# Develop a program that reads the first term and the common difference of an arithmetic progression (AP). Finally, display the first 10 terms of this progression. 🇺🇸
# Desarrolla un programa que lea el primer término y la diferencia común de una progresión aritmética (PA). Finalmente, muestra los primeros 10 términos de esta progresión. 🇪🇸
# Concevez un programme qui lit le premier terme et la raison d'une suite arithmétique. Enfin, affichez les 10 premiers termes de cette suite. 🇫🇷

print("ARITHMETIC PROGRESSION")
p_termo = int(input("Enter the first term of an arithmetic progression (AP): "))
razao = int(input("Enter the common difference for this arithmetic progression (AP): "))
dec = p_termo + (10 - 1) * razao

print("The first ten terms of this arithmetic progression are:", end=" ")
for i in range(p_termo, dec + razao, razao):
    print(f"{i}", end=" → ")
print("END.")
