# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 🇧🇷
# Write a program that reads a young person's birth year and, based on their age, indicates whether they are still going to register for military service, whether it's time to register, or whether they have already missed the registration deadline. Your program should also show how much time is left or how long it has passed since the deadline. 🇺🇸
# Escriba un programa que lea el año de nacimiento de un joven y, según su edad, indique si aún se inscribirá en el servicio militar, si es el momento de inscribirse o si ya se le pasó la fecha límite de inscripción. El programa también debe mostrar cuánto tiempo le queda o cuánto tiempo ha transcurrido desde la fecha límite. 🇪🇸
# Écrivez un programme qui, à partir de l'année de naissance d'un jeune, indique s'il souhaite encore s'inscrire au service militaire, s'il est temps de le faire ou s'il a déjà dépassé la date limite. Votre programme doit également afficher le temps restant ou le temps écoulé depuis la date limite. 🇫🇷

from datetime import date

current_year = date.today().year
year_birth = int(input("Enter the year of birth of a young person: "))

age =  current_year - year_birth
time = 18 - age

if age < 18:
    if time > 1:
        print(f"This young man ({age} years old) still has to register for military service.. There are {time} years left until the {year_birth + 18} Military Registration.")
    else:
        print(f"This young man ({age} years old) still has to register for military service.. There is {time} year left until the {year_birth + 18} Military Registration.")
elif age == 18:
    print(f"It's time for this young man ({age} years old) to register for military service. Good luck with the {year_birth + 18} Military Registration.")
else:
    delay = age - 18
    if delay > 1:
        print(f"It's long past time for this young man ({age} years old) to register for military service. {delay} years have passed since the {year_birth + 18} Military Registration deadline.")
    else:
        print(f"It's long past time for this young man ({age} years old) to register for military service. {delay} year has passed since the {year_birth + 18} Military Registration deadline.")
