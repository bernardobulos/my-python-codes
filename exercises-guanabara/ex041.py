# A Condeferação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos = Mirim; Até 14 anos = Infantil; Até 19 anos = Júnior; Até 25 anos = Sênior; e acima de 25 anos = Mestre. 🇧🇷
# The National Swimming Confederation needs a program that reads an athlete's year of birth and displays their category according to age: Up to 9 years = Children; Up to 14 years = Youth; Up to 19 years = Junior; Up to 25 years = Senior; and over 25 years = Master. 🇺🇸
# La Confederación Nacional de Natación necesita un programa que lea el año de nacimiento de un atleta y muestre su categoría según la edad: Hasta 9 años = Niños; Hasta 14 años = Jóvenes; Hasta 19 años = Junior; Hasta 25 años = Senior; y más de 25 años = Master. 🇪🇸
# La Confédération nationale de natation a besoin d'un programme qui lise l'année de naissance d'un athlète et affiche sa catégorie en fonction de son âge : jusqu'à 9 ans = Enfants ; jusqu'à 14 ans = Jeunes ; jusqu'à 19 ans = Juniors ; jusqu'à 25 ans = Seniors ; et plus de 25 ans = Masters. 🇫🇷

from datetime import date

print("NATIONAL SWIMMING CONFEDERATION")
year_birth = int(input("Enter the year of birth of an athlete: "))
current_year = date.today().year
age = current_year - year_birth

if age <= 9:
    print(f"This athlete ({age} years old) is in the Children category.")
elif 10 <= age <= 14:
    print(f"This athlete ({age} years old) is in the Youth category.")
elif 15 <= age <= 19:
    print(f"This athlete ({age} years old) is in the Junior category.")
elif 20 <= age <= 25:
    print(f"This athlete ({age} years old) is in the Senior category.")
else:
    print(f"This athlete ({age} years old) is in the Master category.")
