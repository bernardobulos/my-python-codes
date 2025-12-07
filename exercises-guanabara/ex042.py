# Refaça o desafio ex035.py dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Esquilátero se todos os lados forem iguais; Isóceles se apenas dois lados forem iguais; e Escaleno se todos os lados forem diferentes. 🇧🇷
# Redo the triangle challenge ex035.py, adding the feature to show what type of triangle will be formed: Schilateral if all sides are equal; Isosceles if only two sides are equal; and Scalene if all sides are different. 🇺🇸
# Rehaga el desafío del triángulo ex035.py, agregando la característica para mostrar qué tipo de triángulo se formará: esquilátero si todos los lados son iguales; isósceles si solo dos lados son iguales; y escaleno si todos los lados son diferentes. 🇪🇸
# Refaites le défi du triangle ex035.py, en ajoutant la fonctionnalité pour afficher quel type de triangle sera formé : schilatéral si tous les côtés sont égaux ; isocèle si seulement deux côtés sont égaux ; et scalène si tous les côtés sont différents. 🇫🇷

print("CONDITION FOR THE EXISTENCE OF A TRIANGLE")
a = float(input("Type the first line of a triangle: "))
b = float(input("Type the second line of a triangle: "))
c = float(input("Type the third line of a triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The lengths of the three lines can form an ", end="")
    if a == b == c:
        print("\033[32mequilateral\033[m triangle.")
    elif a == b != c or a == c != b or c == b != a:
        print("\033[32misosceles\033[m triangle.")
    else:
        print("\033[32mscalene\033[m triangle.")
else:
    print("The lengths of the three lines cannot form a triangle.")
